#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import utilities.common
from py_privatekonomi.utilities.common import format_time_struct, is_unicode
from py_privatekonomi.utilities import helper
from py_privatekonomi.core import loader
from py_privatekonomi.core.error import MissingAppFunctionError
class TestErrors(unittest.TestCase):
    def setUp(self):
        pass

    def test_missing_app_function_error(self):
        app = loader.load_app(
            app_name='py_privatekonomi.core.apps.default',
            sources='samples/swedbank/sample1',
            parser_name='swedbank',
            formatter_name='swedbank',
            persist=True)
        self.assertRaises(MissingAppFunctionError, helper.execute_app, app)

if __name__ == '__main__':
    unittest.main()