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
from py_privatekonomi.tests.dataset.nordnet.sample1 import test_data as test_data_1

class TestNordnet(TestBase):
    def setUp(self):
        pass

    def test_sample1(self):
        app = loader.load_app(
            app_name='py_privatekonomi.core.apps.default',
            sources='samples/nordnet/sample1.csv',
            parser_name='nordnet',
            formatter_name='nordnet')
        results = helper.execute_app(app)
        self.assertFormatted(results, test_data_1, format_as_mapper=False)

    def test_excel(self):
        app = loader.load_app(
            app_name='py_privatekonomi.core.apps.default',
            sources='samples/nordnet/excel_sample.xlsx',
            parser_name='nordnet',
            formatter_name='nordnet')
        results = helper.execute_app(app)
        self.assertFormatted(results, test_data_1, format_as_mapper=False)

if __name__ == '__main__':
    unittest.main()