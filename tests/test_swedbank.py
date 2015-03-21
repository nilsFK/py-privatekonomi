#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import loader
import utilities.common
from utilities.common import format_time_struct, is_unicode
from utilities import helper
from core.error import FormatterError, ParserError
from test_base import TestBase
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

        for r in results:
            self.assertEqual(format_time_struct(r[0]["accounting_date"]), '2015-01-05')
            self.assertEqual(format_time_struct(r[1]["accounting_date"]), '2015-01-02')
            self.assertEqual(format_time_struct(r[2]["accounting_date"]), '2015-01-02')
            self.assertEqual(format_time_struct(r[3]["accounting_date"]), '2015-01-02')
            self.assertEqual(format_time_struct(r[4]["accounting_date"]), '2015-01-02')
            self.assertEqual(format_time_struct(r[5]["accounting_date"]), '2014-12-29')
            self.assertEqual(format_time_struct(r[6]["accounting_date"]), '2014-12-29')

            self.assertEqual(format_time_struct(r[0]["transaction_date"]), '2015-01-03')
            self.assertEqual(format_time_struct(r[1]["transaction_date"]), '2015-01-02')
            self.assertEqual(format_time_struct(r[2]["transaction_date"]), '2015-01-02')
            self.assertEqual(format_time_struct(r[3]["transaction_date"]), '2015-01-02')
            self.assertEqual(format_time_struct(r[4]["transaction_date"]), '2015-01-01')
            self.assertEqual(format_time_struct(r[5]["transaction_date"]), '2014-12-28')
            self.assertEqual(format_time_struct(r[6]["transaction_date"]), '2014-12-27')

            self.assertEqual(r[0]["account_reference"], u"PATREON.COM")
            self.assertEqual(r[1]["account_reference"], u"PATREON.COM")
            self.assertEqual(r[2]["account_reference"], u"BURGER KING")
            self.assertEqual(r[3]["account_reference"], u"ICA SUPERMARKET")
            self.assertEqual(r[4]["account_reference"], u"ICA SUPERMARKET")
            self.assertEqual(r[5]["account_reference"], u"McDonalds")
            self.assertEqual(r[6]["account_reference"], u"SPOTIFY Spotify")

            self.assertEqual(r[0]["amount"], -8.02)
            self.assertEqual(r[1]["amount"], -7.96)
            self.assertEqual(r[2]["amount"], -69.0)
            self.assertEqual(r[3]["amount"], -93.97)
            self.assertEqual(r[4]["amount"], -88.60)
            self.assertEqual(r[5]["amount"], -75.0)
            self.assertEqual(r[6]["amount"], -49.0)

            self.assertEqual(r[0]["balance"], 6560.18)
            self.assertEqual(r[1]["balance"], 16061.26)
            self.assertEqual(r[2]["balance"], 16069.22)
            self.assertEqual(r[3]["balance"], 16138.22)
            self.assertEqual(r[4]["balance"], 16232.19)
            self.assertEqual(r[5]["balance"], 17066.54)
            self.assertEqual(r[6]["balance"], 17141.54)

    def test_sample2(self):
        app = loader.load_app(
            app_name='core.apps.default',
            sources='samples/swedbank/sample2',
            parser_name='swedbank',
            formatter_name='swedbank')
        results = helper.execute_app(app)

        for r in results:
            self.assertEqual(r[0]["clearing_number"], '12345')
            self.assertEqual(r[1]["clearing_number"], '12345')
            self.assertEqual(r[3]["clearing_number"], '12345')
            self.assertEqual(r[4]["clearing_number"], '12345')
            self.assertEqual(r[5]["clearing_number"], '12345')
            self.assertEqual(r[6]["clearing_number"], '12345')
            self.assertEqual(r[7]["clearing_number"], '12345')
            self.assertEqual(r[8]["clearing_number"], '12345')
            self.assertEqual(r[9]["clearing_number"], '12345')
            self.assertEqual(r[10]["clearing_number"], '12345')

            self.assertEqual(r[0]["account_number"], '1234567890')
            self.assertEqual(r[1]["account_number"], '1234567890')
            self.assertEqual(r[2]["account_number"], '1234567890')
            self.assertEqual(r[3]["account_number"], '1234567890')
            self.assertEqual(r[4]["account_number"], '1234567890')
            self.assertEqual(r[5]["account_number"], '1234567890')
            self.assertEqual(r[6]["account_number"], '1234567890')
            self.assertEqual(r[7]["account_number"], '1234567890')
            self.assertEqual(r[8]["account_number"], '1234567890')
            self.assertEqual(r[9]["account_number"], '1234567890')
            self.assertEqual(r[10]["account_number"], '1234567890')

            self.assertEqual(r[0]["account_name"], u'Mitt vanliga konto')
            self.assertEqual(r[1]["account_name"], u'Mitt vanliga konto')
            self.assertEqual(r[2]["account_name"], u'Mitt vanliga konto')
            self.assertEqual(r[3]["account_name"], u'Mitt vanliga konto')
            self.assertEqual(r[4]["account_name"], u'Mitt vanliga konto')
            self.assertEqual(r[5]["account_name"], u'Mitt vanliga konto')
            self.assertEqual(r[6]["account_name"], u'Mitt vanliga konto')
            self.assertEqual(r[7]["account_name"], u'Mitt vanliga konto')
            self.assertEqual(r[8]["account_name"], u'Mitt vanliga konto')
            self.assertEqual(r[9]["account_name"], u'Mitt vanliga konto')
            self.assertEqual(r[10]["account_name"], u'Mitt vanliga konto')

            self.assertEqual(r[0]["currency_code"], u'SEK')
            self.assertEqual(r[1]["currency_code"], u'SEK')
            self.assertEqual(r[2]["currency_code"], u'SEK')
            self.assertEqual(r[3]["currency_code"], u'SEK')
            self.assertEqual(r[4]["currency_code"], u'SEK')
            self.assertEqual(r[5]["currency_code"], u'SEK')
            self.assertEqual(r[6]["currency_code"], u'SEK')
            self.assertEqual(r[7]["currency_code"], u'SEK')
            self.assertEqual(r[8]["currency_code"], u'SEK')
            self.assertEqual(r[9]["currency_code"], u'SEK')
            self.assertEqual(r[10]["currency_code"], u'SEK')

            self.assertEqual(format_time_struct(r[0]["accounting_date"]), '2015-01-05')
            self.assertEqual(format_time_struct(r[1]["accounting_date"]), '2015-01-02')
            self.assertEqual(format_time_struct(r[2]["accounting_date"]), '2015-01-02')
            self.assertEqual(format_time_struct(r[3]["accounting_date"]), '2015-01-02')
            self.assertEqual(format_time_struct(r[4]["accounting_date"]), '2015-01-02')
            self.assertEqual(format_time_struct(r[5]["accounting_date"]), '2014-12-29')
            self.assertEqual(format_time_struct(r[6]["accounting_date"]), '2014-12-29')
            self.assertEqual(format_time_struct(r[7]["accounting_date"]), '2014-12-23')
            self.assertEqual(format_time_struct(r[8]["accounting_date"]), '2014-12-23')
            self.assertEqual(format_time_struct(r[9]["accounting_date"]), '2014-12-23')
            self.assertEqual(format_time_struct(r[10]["accounting_date"]), '2014-12-22')

            self.assertEqual(format_time_struct(r[0]["transaction_date"]), '2015-01-03')
            self.assertEqual(format_time_struct(r[1]["transaction_date"]), '2015-01-02')
            self.assertEqual(format_time_struct(r[2]["transaction_date"]), '2015-01-02')
            self.assertEqual(format_time_struct(r[3]["transaction_date"]), '2015-01-01')
            self.assertEqual(format_time_struct(r[4]["transaction_date"]), '2014-12-31')
            self.assertEqual(format_time_struct(r[5]["transaction_date"]), '2014-12-27')
            self.assertEqual(format_time_struct(r[6]["transaction_date"]), '2014-12-24')
            self.assertEqual(format_time_struct(r[7]["transaction_date"]), '2014-12-23')
            self.assertEqual(format_time_struct(r[8]["transaction_date"]), '2014-12-23')
            self.assertEqual(format_time_struct(r[9]["transaction_date"]), '2014-12-23')
            self.assertEqual(format_time_struct(r[10]["transaction_date"]), '2014-12-22')

            self.assertEqual(r[0]["account_reference"], u'PATREON.COM')
            self.assertEqual(r[1]["account_reference"], u'PATREON.COM')
            self.assertEqual(r[2]["account_reference"], u'ICA SUPERMARKET')
            self.assertEqual(r[3]["account_reference"], u'ICA SUPERMARKET')
            self.assertEqual(r[4]["account_reference"], u'ICA SUPERMARKET')
            self.assertEqual(r[5]["account_reference"], u'SPOTIFY Spotify')
            self.assertEqual(r[6]["account_reference"], u'ELGIGANTEN STOC')
            self.assertEqual(r[7]["account_reference"], u'HBONORDIC.COM')
            self.assertEqual(r[8]["account_reference"], u'BAR BQ BAR & GRI')
            self.assertEqual(r[9]["account_reference"], u'COOP KONSUM')
            self.assertEqual(r[10]["account_reference"], u'')

            self.assertEqual(r[0]["account_event"], u'Kortköp/uttag')
            self.assertEqual(r[1]["account_event"], u'Kortköp/uttag')
            self.assertEqual(r[2]["account_event"], u'Kortköp/uttag')
            self.assertEqual(r[3]["account_event"], u'Kortköp/uttag')
            self.assertEqual(r[4]["account_event"], u'Kortköp/uttag')
            self.assertEqual(r[5]["account_event"], u'Kortköp/uttag')
            self.assertEqual(r[6]["account_event"], u'Kortköp/uttag')
            self.assertEqual(r[7]["account_event"], u'Kortköp/uttag')
            self.assertEqual(r[8]["account_event"], u'Kortköp/uttag')
            self.assertEqual(r[9]["account_event"], u'Kortköp/uttag')
            self.assertEqual(r[10]["account_event"], u'Kortköp/uttag')

            self.assertEqual(r[0]["amount"], -8.02)
            self.assertEqual(r[1]["amount"], -7.96)
            self.assertEqual(r[2]["amount"], -93.97)
            self.assertEqual(r[3]["amount"], -88.60)
            self.assertEqual(r[4]["amount"], -315.29)
            self.assertEqual(r[5]["amount"], -49.0)
            self.assertEqual(r[6]["amount"], -1490.0)
            self.assertEqual(r[7]["amount"], -79.0)
            self.assertEqual(r[8]["amount"], -72.0)
            self.assertEqual(r[9]["amount"], -103.94)
            self.assertEqual(r[10]["amount"], -1000.0)

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