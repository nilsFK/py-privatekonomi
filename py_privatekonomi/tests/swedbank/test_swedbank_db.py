#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import unittest
import inspect
from py_privatekonomi.utilities import common
from py_privatekonomi.tests.test_base import TestBase
from py_privatekonomi.tests.dataset.swedbank.sample1 import test_data as test_data_1
from py_privatekonomi.tests.dataset.swedbank.sample2 import test_data as test_data_2
from py_privatekonomi.tests.dataset.swedbank.sample3 import test_data as test_data_3
from py_privatekonomi.tests.dataset.swedbank.sample5 import test_data as test_data_5
class TestSwedbankDB(TestBase):
    def setUp(self):
        pass

    def test_sample1_db(self):
        results = self.executeApp('py_privatekonomi.core.apps.example3',
            'samples/swedbank/sample1',
            'swedbank',
            'swedbank',
            persist=True,
            config=self.get_default_config())
        if results is False:
            print(("Skipping:", inspect.stack()[0][3]))
        else:
            self.assertFormatted(results, test_data_1, format_as_mapper=True)
            self.assertPersisted(test_data_1)

    def test_sample2_db(self):
        results = self.executeApp('py_privatekonomi.core.apps.example3',
            'samples/swedbank/sample2',
            'swedbank',
            'swedbank',
            persist=True,
            config=self.get_default_config())
        if results is False:
            print(("Skipping:", inspect.stack()[0][3]))
        else:
            self.assertFormatted(results, test_data_2, format_as_mapper=True)
            self.assertPersisted(test_data_2)

    def test_sample3_db(self):
        results = self.executeApp('py_privatekonomi.core.apps.example3',
            'samples/swedbank/sample3',
            'swedbank',
            'swedbank',
            config=self.get_default_config(),
            persist=True)
        if results is False:
            print(("Skipping:", inspect.stack()[0][3]))
        else:
            self.assertFormatted(results, test_data_3, format_as_mapper=True)
            self.assertPersisted(test_data_3)

    def test_sample5_db(self):
        results = self.executeApp('py_privatekonomi.core.apps.example3',
            'samples/swedbank/sample5',
            'swedbank',
            'swedbank',
            config=self.get_default_config(),
            persist=True)
        if results is False:
            print(("Skipping:", inspect.stack()[0][3]))
        else:
            self.assertFormatted(results, test_data_5, format_as_mapper=True)
            self.assertPersisted(test_data_5)


if __name__ == '__main__':
    unittest.main()