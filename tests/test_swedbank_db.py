#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import loader
import inspect
import utilities.common
from utilities.common import format_time_struct, is_unicode
from utilities import helper
from core.error import FormatterError, ParserError
from test_base import TestBase
class TestSwedbank(TestBase):
    def setUp(self):
        pass

    def test_sample1_db(self):
        results = self.executeApp('core.apps.example3',
            'samples/swedbank/sample1',
            'swedbank',
            'swedbank',
            True)
        if results is False:
            print("Skipping:", inspect.stack()[0][3])

    def test_sample2_db(self):
        results = self.executeApp('core.apps.example3',
            'samples/swedbank/sample2',
            'swedbank',
            'swedbank',
            True)
        if results is False:
            print("Skipping:", inspect.stack()[0][3])

    def test_sample3_db(self):
        results = self.executeApp('core.apps.example3',
            'samples/swedbank/sample3',
            'swedbank',
            'swedbank',
            True)
        if results is False:
            print("Skipping:", inspect.stack()[0][3])


if __name__ == '__main__':
    unittest.main()