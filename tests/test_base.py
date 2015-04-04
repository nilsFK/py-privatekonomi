#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import unittest
from utilities.common import format_time_struct, is_unicode
from utilities import helper
import utilities.common
import loader
try:
    # 2.x.x
    import ConfigParser
    from ConfigParser import SafeConfigParser as config_parser
except:
    # 3.x.x
    import configparser as ConfigParser
    from configparser import ConfigParser as config_parser
class TestBase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)

    def __assertEquals(self, equals_from, equals_to, msg=None):
        super(TestBase, self).assertEqual(utilities.common.decode(equals_from), utilities.common.decode(equals_to), msg)

    def assertEqual(self, a, b, msg=None):
        self.__assertEquals(a, b, msg)

    def assertTrue(self, x, msg):
        raise NotImplementedError

    def assertFalse(self, y, msg):
        raise NotImplementedError

    def assertIs(self, a, b, msg):
        raise NotImplementedError

    def assertIsNot(self, a, b, msg):
        raise NotImplementedError

    # def assertIsNone(self, x):
    #     raise NotImplementedError

    # def assertIsNotNone(self, x):
    #     raise NotImplementedError

    def assertIn(self, a, b, msg):
        raise NotImplementedError

    def assertNotIn(self, a, b, msg):
        raise NotImplementedError

    # def assertIsInstance(self, a, b):
    #     raise NotImplementedError

    # def assertNotIsInstance(self, a, b):
    #     raise NotImplementedError

    def executeApp(self, app_name, sources, parser_name, formatter_name, persist = False):
        file_config = None if persist is False else "db_test"
        try:
            app = loader.load_app(
                app_name=app_name,
                sources=sources,
                parser_name=parser_name,
                formatter_name=formatter_name,
                persist=persist)
            results = helper.execute_app(app, file_config)
        except ConfigParser.NoSectionError:
            results = False
        return results

    def assertFormatted(self, models_data, expected, key_models=False):
        for model_data in models_data:
            for idx, data in enumerate(model_data):
                try:
                    next_expected = expected[idx]
                except IndexError:
                    raise Exception("Expected data is missing index: %s (from expected dataset %s)" % (idx, expected))
                if key_models is True:
                    for model_name in data.keys():
                        if model_name not in next_expected:
                            raise Exception("Missing model: %s in (%s)" % (model_name, next_expected))
                        for col in next_expected[model_name].keys():
                            val = next_expected[model_name][col]
                            self.assertEqual(val, data[model_name][col], "%s.%s %s is not equal to %s.%s %s in index %s (comparing subdata %s with %s)" % (model_name, col, val, model_name, col, data[model_name][col], idx, next_expected, data[model_name]))
                else:
                    raise NotImplementedError
