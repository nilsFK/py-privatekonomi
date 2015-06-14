#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import loader
from py_privatekonomi.utilities.common import format_time_struct, is_unicode
from py_privatekonomi.utilities import helper
from py_privatekonomi.core.error import FormatterError, ParserError
from test_base import TestBase
from py_privatekonomi.tests.dataset.avanza.sample1 import test_data as test_data_1

class TestAvanza(TestBase):
    def setUp(self):
        pass

    def test_sample1(self):
        app = loader.load_app(
            app_name='py_privatekonomi.core.apps.default',
            sources='samples/avanza/sample1',
            parser_name='avanza',
            formatter_name='avanza')
        results = helper.execute_app(app)

        self.assertFormatted(results, test_data_1, format_as_mapper=False)

    def test_invalid_sample1(self):
        """ Test invalid transaction file which throws FormatterError """
        app =  loader.load_app(
            app_name='py_privatekonomi.core.apps.default',
            sources='samples/invalid/avanza/invalid_sample1',
            parser_name='avanza',
            formatter_name='avanza')
        self.assertRaises(FormatterError, helper.execute_app, app)

    def test_invalid_sample2(self):
        """ Test invalid transaction file which throws ParserError """
        app =  loader.load_app(
            app_name='py_privatekonomi.core.apps.default',
            sources='samples/invalid/avanza/invalid_sample2',
            parser_name='avanza',
            formatter_name='avanza')
        self.assertRaises(FormatterError, helper.execute_app, app)

if __name__ == '__main__':
    unittest.main()