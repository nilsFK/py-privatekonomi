#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import loader
import utilities.common
from utilities.common import format_time_struct, is_unicode
from utilities import helper
from core.error import FormatterError, ParserError
class TestAvanza(unittest.TestCase):
    def setUp(self):
        pass

    def test_sample1(self):
        app = loader.load_app(
            app_name='core.apps.example1',
            sources='samples/avanza/sample1',
            parser_name='avanza',
            formatter_name='avanza')
        results = helper.execute_app(app)

        for r in results:
            self.assertEquality(format_time_struct(r[0]["transaction_date"]), '2015-01-08')
            self.assertEquality(format_time_struct(r[1]["transaction_date"]), '2015-01-07')
            self.assertEquality(format_time_struct(r[2]["transaction_date"]), '2015-01-07')
            self.assertEquality(format_time_struct(r[3]["transaction_date"]), '2015-01-05')
            self.assertEquality(format_time_struct(r[4]["transaction_date"]), '2014-12-08')
            self.assertEquality(format_time_struct(r[5]["transaction_date"]), '2014-11-26')
            self.assertEquality(format_time_struct(r[6]["transaction_date"]), '2014-10-29')
            self.assertEquality(format_time_struct(r[7]["transaction_date"]), '2014-10-28')
            self.assertEquality(format_time_struct(r[8]["transaction_date"]), '2014-10-27')
            self.assertEquality(format_time_struct(r[9]["transaction_date"]), '2014-10-02')

            self.assertEquality(r[0]["account_name"], u"Spar Aktie")
            self.assertEquality(r[1]["account_name"], u"Spar Aktie")
            self.assertEquality(r[2]["account_name"], u"Spar Aktie")
            self.assertEquality(r[3]["account_name"], u"Spar Aktie")
            self.assertEquality(r[4]["account_name"], u"Spar Aktie")
            self.assertEquality(r[5]["account_name"], u"Spar Aktie")
            self.assertEquality(r[6]["account_name"], u"Spar Aktie")
            self.assertEquality(r[7]["account_name"], u"Spar Aktie")
            self.assertEquality(r[8]["account_name"], u"Spar Aktie")
            self.assertEquality(r[9]["account_name"], u"Spar Aktie")

            self.assertEquality(r[0]["transaction_event"], u"Sälj")
            self.assertEquality(r[1]["transaction_event"], u"Köp")
            self.assertEquality(r[2]["transaction_event"], u"Köp")
            self.assertEquality(r[3]["transaction_event"], u"Insättning")
            self.assertEquality(r[4]["transaction_event"], u"Köp")
            self.assertEquality(r[5]["transaction_event"], u"Insättning")
            self.assertEquality(r[6]["transaction_event"], u"Köp")
            self.assertEquality(r[7]["transaction_event"], u"Köp")
            self.assertEquality(r[8]["transaction_event"], u"Insättning")
            self.assertEquality(r[9]["transaction_event"], u"Köp")

            self.assertEquality(r[0]["security_name"], u"Aktiefond #1")
            self.assertEquality(r[1]["security_name"], u"Aktiefond #2")
            self.assertEquality(r[2]["security_name"], u"Aktiefond #3")
            self.assertEquality(r[3]["security_name"], u"Insättning Januari")
            self.assertEquality(r[4]["security_name"], u"Aktiefond #2")
            self.assertEquality(r[5]["security_name"], u"Insättning November")
            self.assertEquality(r[6]["security_name"], u"Aktiefond #3")
            self.assertEquality(r[7]["security_name"], u"Aktiefond #2")
            self.assertEquality(r[8]["security_name"], u"Insättning Oktober")
            self.assertEquality(r[9]["security_name"], u"Aktiefond #1")

            self.assertEquality(r[0]["security_amount"], 4.0726)
            self.assertEquality(r[1]["security_amount"], 15.1663)
            self.assertEquality(r[2]["security_amount"], 0.8534)
            self.assertEquality(r[3]["security_amount"], None)
            self.assertEquality(r[4]["security_amount"], 5.1423)
            self.assertEquality(r[5]["security_amount"], None)
            self.assertEquality(r[6]["security_amount"], 16.2254)
            self.assertEquality(r[7]["security_amount"], 8.7321)
            self.assertEquality(r[8]["security_amount"], None)
            self.assertEquality(r[9]["security_amount"], 149.8263)

            self.assertEquality(r[0]["security_rate"], 413.68)
            self.assertEquality(r[1]["security_rate"], 222.17)
            self.assertEquality(r[2]["security_rate"], 1974.0)
            self.assertEquality(r[3]["security_rate"], None)
            self.assertEquality(r[4]["security_rate"], 222.66)
            self.assertEquality(r[5]["security_rate"], None)
            self.assertEquality(r[6]["security_rate"], 114.87)
            self.assertEquality(r[7]["security_rate"], 213.35)
            self.assertEquality(r[8]["security_rate"], None)
            self.assertEquality(r[9]["security_rate"], 114.92)

            self.assertEquality(r[0]["transaction_amount"], -1286.75)
            self.assertEquality(r[1]["transaction_amount"], -1329.5)
            self.assertEquality(r[2]["transaction_amount"], -682.61)
            self.assertEquality(r[3]["transaction_amount"], 2728.8)
            self.assertEquality(r[4]["transaction_amount"], -1144.98)
            self.assertEquality(r[5]["transaction_amount"], 2145.42)
            self.assertEquality(r[6]["transaction_amount"], -863.81)
            self.assertEquality(r[7]["transaction_amount"], -862.99)
            self.assertEquality(r[8]["transaction_amount"], 2826.80)
            self.assertEquality(r[9]["transaction_amount"], -10218.04)

            self.assertEquality(r[0]["transaction_currency_code"], u"SEK")
            self.assertEquality(r[1]["transaction_currency_code"], u"SEK")
            self.assertEquality(r[2]["transaction_currency_code"], u"SEK")
            self.assertEquality(r[3]["transaction_currency_code"], u"SEK")
            self.assertEquality(r[4]["transaction_currency_code"], u"SEK")
            self.assertEquality(r[5]["transaction_currency_code"], u"SEK")
            self.assertEquality(r[6]["transaction_currency_code"], u"SEK")
            self.assertEquality(r[7]["transaction_currency_code"], u"SEK")
            self.assertEquality(r[8]["transaction_currency_code"], u"SEK")
            self.assertEquality(r[9]["transaction_currency_code"], u"SEK")

    def test_invalid_sample1(self):
        """ Test invalid transaction file which throws FormatterError """
        app =  loader.load_app(
            app_name='core.apps.example1',
            sources='samples/invalid/avanza/invalid_sample1',
            parser_name='avanza',
            formatter_name='avanza')
        self.assertRaises(FormatterError, helper.execute_app, app)

    def test_invalid_sample2(self):
        """ Test invalid transaction file which throws ParserError """
        app =  loader.load_app(
            app_name='core.apps.example1',
            sources='samples/invalid/avanza/invalid_sample2',
            parser_name='avanza',
            formatter_name='avanza')
        self.assertRaises(FormatterError, helper.execute_app, app)

    def assertEquality(self, equals_from, equals_to):
        self.assertEqual(utilities.common.decode(equals_from), utilities.common.decode(equals_to))

if __name__ == '__main__':
    unittest.main()