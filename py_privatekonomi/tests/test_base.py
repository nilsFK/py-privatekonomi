#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from __future__ import absolute_import
from __future__ import unicode_literals
import unittest
from py_privatekonomi.utilities.common import format_time_struct, is_unicode, is_time_struct, as_obj
from py_privatekonomi.utilities.models import get_models
from py_privatekonomi.utilities import helper, common
from py_privatekonomi.core.mappers.economy_mapper import EconomyMapper
from py_privatekonomi.core import config, loader
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
        super(TestBase, self).assertEqual(common.decode(equals_from), common.decode(equals_to), msg)

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

    def get_default_config(self):
        db_config = config.readConfig("db_test", "Database")
        __config = {
            'insert_rows' : 1,
            'use_logging' : False,
            'log_to_file' : False,
            'database' : db_config
        }
        return __config

    def executeApp(self, app_name, sources, parser_name, formatter_name, config = {}, persist = False):
        try:
            app = loader.load_app(
                app_name=app_name,
                sources=sources,
                parser_name=parser_name,
                formatter_name=formatter_name,
                persist=persist)
            results = helper.execute_app(app, as_obj(config))
        except ConfigParser.NoSectionError:
            results = False
        return results

    def assertFormatted(self, models_data, expected, format_as_mapper=False):
        for model_data in models_data:
            for idx, data in enumerate(model_data):
                try:
                    next_expected = expected[idx]
                except IndexError:
                    raise Exception("Expected data is missing index: %s (from expected dataset %s)" % (idx, expected))
                if format_as_mapper is True:
                    for model_name in data.keys():
                        if model_name not in next_expected:
                            raise Exception("Missing model: %s in (%s)" % (model_name, next_expected))
                        for col in next_expected[model_name].keys():
                            val1 = next_expected[model_name][col]
                            val2 = data[model_name][col]
                            if is_time_struct(val2):
                                val2 = format_time_struct(val2)
                            self.assertEqual(val1, val2, "%s.%s %s is not equal to %s.%s %s in index %s (comparing subdata %s with %s)" % (model_name, col, val1, model_name, col, data[model_name][col], idx, next_expected, data[model_name]))
                else:
                    for model_name in next_expected:
                        for col in next_expected[model_name].keys():
                            val = next_expected[model_name][col]
                            col_name = common.camelcase_to_underscore(model_name) + "_" + col

                            if is_time_struct(data[col_name]):
                                self.assertEqual(val, format_time_struct(data[col_name]))
                            else:
                                self.assertEqual(val, data[col_name])

    def assertPersisted(self, expected):
        # TODO assert that other models have been persisted as well
        models = get_models(loader.load_models(["Transaction"]), False)
        transaction_model = models["Transaction"]
        col_names = [col_name for col_name in expected[0]["Transaction"]]
        db_results = transaction_model.getResults(transaction_model.get(), col_names, decode=True)

        for idx, e in enumerate(expected):
            db_res = db_results[idx]
            for col in col_names:
                db_val = db_results[idx][col]
                db_val = transaction_model.decode(db_val)
                self.assertEqual(e["Transaction"][col], db_val)
