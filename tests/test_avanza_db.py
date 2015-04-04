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
from tests.dataset.avanza.sample1 import test_data as test_data_1
class TestAvanza(TestBase):
    def setUp(self):
        pass

    def test_sample1_db(self):
        results = self.executeApp('core.apps.example3',
            'samples/avanza/sample1',
            'avanza',
            'avanza',
            True)
        if results is False:
            print("Skipping:", inspect.stack()[0][3])
        else:
            self.assertFormatted(results, test_data_1, True)

if __name__ == '__main__':
    unittest.main()