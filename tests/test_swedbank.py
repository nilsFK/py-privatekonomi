#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import loader
import utilities.common
from utilities.common import format_time_struct, is_unicode
from utilities import helper
from core.error import FormatterError, ParserError
from test_base import TestBase
from tests.dataset.swedbank.sample1 import test_data as test_data_1
from tests.dataset.swedbank.sample2 import test_data as test_data_2
class TestSwedbank(TestBase):
    def setUp(self):
        pass

    def test_sample1(self):
        app = loader.load_app(
            app_name='core.apps.default',
            sources='samples/swedbank/sample1',
            parser_name='swedbank',
            formatter_name='swedbank')
        results = helper.execute_app(app)

        self.assertFormatted(results, test_data_1, format_as_mapper=False)

    def test_sample2(self):
        app = loader.load_app(
            app_name='core.apps.default',
            sources='samples/swedbank/sample2',
            parser_name='swedbank',
            formatter_name='swedbank')
        results = helper.execute_app(app)

        self.assertFormatted(results, test_data_2, format_as_mapper=False)

    def test_invalid_sample1(self):
        """ Test invalid transaction file which throws FormatterError """
        app = loader.load_app(
            app_name='core.apps.default',
            sources='samples/invalid/swedbank/invalid_sample1',
            parser_name='swedbank',
            formatter_name='swedbank')
        self.assertRaises(FormatterError, helper.execute_app, app)

    def test_invalid_sample2(self):
        """ Test invalid transaction file which throws ParserError """
        app = loader.load_app(
            app_name='core.apps.default',
            sources='samples/invalid/swedbank/invalid_sample2',
            parser_name='swedbank',
            formatter_name='swedbank')
        self.assertRaises(ParserError, helper.execute_app, app)

if __name__ == '__main__':
    unittest.main()