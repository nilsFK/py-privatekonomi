#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals
import unittest
from py_privatekonomi.utilities.common import format_time_struct, is_unicode
from py_privatekonomi.utilities import helper
from py_privatekonomi.core import loader
from py_privatekonomi.core.error import FormatterError, ParserError
from py_privatekonomi.tests.test_base import TestBase
from py_privatekonomi.tests.dataset.avanza.sample1 import test_data as test_data_1
from py_privatekonomi.tests.dataset.avanza.excel_sample import test_data as test_data_excel

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

    def test_sample2(self):
        """ sample2 is a copy of sample1 containing three empty rows which should be ignored """
        app = loader.load_app(
            app_name='py_privatekonomi.core.apps.default',
            sources='samples/avanza/sample2',
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

    def test_excel(self):
        """ Test valid excel file """
        app = loader.load_app(
            app_name='py_privatekonomi.core.apps.default',
            sources='samples/avanza/excel_sample.xlsx',
            parser_name='avanza',
            formatter_name='avanza')
        results = helper.execute_app(app)
        self.assertFormatted(results, test_data_excel, format_as_mapper=False)

if __name__ == '__main__':
    unittest.main()