#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from py_privatekonomi.utilities.common import format_time_struct, is_unicode
from py_privatekonomi.utilities import helper
from py_privatekonomi.core import loader
from py_privatekonomi.core.error import FormatterError, ParserError
from py_privatekonomi.tests.test_base import TestBase
from py_privatekonomi.tests.dataset.swedbank.sample1 import test_data as test_data_1
from py_privatekonomi.tests.dataset.swedbank.sample2 import test_data as test_data_2

class TestSwedbank(TestBase):
    def setUp(self):
        pass

    def test_sample1(self):
        app = loader.load_app(
            app_name='py_privatekonomi.core.apps.default',
            sources='samples/swedbank/sample1',
            parser_name='swedbank',
            formatter_name='swedbank')
        config = {}
        config['database'] = self.get_default_config()
        results = helper.execute_app(app, config)
        self.assertFormatted(results, test_data_1, format_as_mapper=False)

    def test_sample2(self):
        app = loader.load_app(
            app_name='py_privatekonomi.core.apps.default',
            sources='samples/swedbank/sample2',
            parser_name='swedbank',
            formatter_name='swedbank')
        results = helper.execute_app(app)
        self.assertFormatted(results, test_data_2, format_as_mapper=False)

    def test_sample4(self):
        """ sample4 is the same as test_data_1 """
        app = loader.load_app(
            app_name='py_privatekonomi.core.apps.default',
            sources='samples/swedbank/sample4',
            parser_name='swedbank',
            formatter_name='swedbank')
        results = helper.execute_app(app)
        self.assertFormatted(results, test_data_1, format_as_mapper=False)

    def test_text_sample(self):
        sources = []
        source = \
"""
15-01-05    15-01-03    PATREON.COM     -8,02   6 560,18
15-01-02    15-01-02    PATREON.COM     -7,96   16 061,26
15-01-02    15-01-02    BURGER KING     -69,00  16 069,22
15-01-02    15-01-02    ICA SUPERMARKET     -93,97  16 138,22
15-01-02    15-01-01    ICA SUPERMARKET     -88,60  16 232,19
14-12-29    14-12-28    McDonalds   -75,00  17 066,54
14-12-29    14-12-27    SPOTIFY Spotify     -49,00  17 141,54
"""
        sources.append(source)
        app = loader.load_app(
            app_name='py_privatekonomi.core.apps.example5',
            sources=sources,
            parser_name='swedbank',
            formatter_name='swedbank'
            )
        results = helper.execute_app(app)
        self.assertFormatted(results, test_data_1, format_as_mapper=False)

    def test_invalid_sample1(self):
        """ Test invalid transaction file which throws FormatterError
            invalid_sample1 contains two spaces in last token, which
            is illegal
        """
        app = loader.load_app(
            app_name='py_privatekonomi.core.apps.default',
            sources='samples/invalid/swedbank/invalid_sample1',
            parser_name='swedbank',
            formatter_name='swedbank')
        self.assertRaises(FormatterError, helper.execute_app, app)

    def test_invalid_sample2(self):
        """ Test invalid transaction file which throws ParserError """
        app = loader.load_app(
            app_name='py_privatekonomi.core.apps.default',
            sources='samples/invalid/swedbank/invalid_sample2',
            parser_name='swedbank',
            formatter_name='swedbank')
        self.assertRaises(ParserError, helper.execute_app, app)

    def test_invalid_excel_file(self):
        """ Test invalid excel file which throws ParserError """
        app = loader.load_app(
            app_name='py_privatekonomi.core.apps.default',
            sources='samples/avanza/excel_sample.xlsx',
            parser_name='swedbank',
            formatter_name='swedbank')
        self.assertRaises(ParserError, helper.execute_app, app)

if __name__ == '__main__':
    unittest.main()