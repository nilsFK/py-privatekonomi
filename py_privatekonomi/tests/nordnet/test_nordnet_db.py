#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import inspect
from py_privatekonomi.tests.test_base import TestBase
from py_privatekonomi.tests.dataset.nordnet.sample1 import test_data as test_data_1
class TestNordnetDB(TestBase):
    def setUp(self):
        pass

    def test_sample1_db(self):
        results = self.executeApp(
            app_name='py_privatekonomi.core.apps.example3',
            sources='samples/nordnet/sample1.csv',
            parser_name='nordnet',
            formatter_name='nordnet',
            persist=True,
            config=self.get_default_config())
        if results is False:
            print("Skipping:", inspect.stack()[0][3])
        else:
            print(repr(results))
            self.assertFormatted(results, test_data_1, format_as_mapper=True)
            self.assertPersisted(test_data_1)

if __name__ == '__main__':
    unittest.main()