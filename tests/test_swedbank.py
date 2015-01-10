#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import apps.main
import time
class TestSwedbank(unittest.TestCase):
    def setUp(self):
        pass

    # def test_sample2(self):
    #     r = apps.main.execute('samples/swedbank/sample2',
    #         parser='swedbank',
    #         formatter='swedbank')
    #     print(r)

    def test_sample1(self):
        r = apps.main.execute('samples/swedbank/sample1',
            parser='swedbank',
            formatter='swedbank')
        print(r)

        print self.format_time_struct(r[0]["transaction_date"])

        self.assertEquals(self.format_time_struct(r[0]["accounting_date"]), '2015-01-05')
        self.assertEquals(self.format_time_struct(r[1]["accounting_date"]), '2015-01-02')
        self.assertEquals(self.format_time_struct(r[2]["accounting_date"]), '2015-01-02')
        self.assertEquals(self.format_time_struct(r[3]["accounting_date"]), '2015-01-02')
        self.assertEquals(self.format_time_struct(r[4]["accounting_date"]), '2015-01-02')
        self.assertEquals(self.format_time_struct(r[5]["accounting_date"]), '2014-12-29')
        self.assertEquals(self.format_time_struct(r[6]["accounting_date"]), '2014-12-29')

        self.assertEquals(self.format_time_struct(r[0]["transaction_date"]), '2015-01-03')
        self.assertEquals(self.format_time_struct(r[1]["transaction_date"]), '2015-01-02')
        self.assertEquals(self.format_time_struct(r[2]["transaction_date"]), '2015-01-02')
        self.assertEquals(self.format_time_struct(r[3]["transaction_date"]), '2015-01-02')
        self.assertEquals(self.format_time_struct(r[4]["transaction_date"]), '2015-01-01')
        self.assertEquals(self.format_time_struct(r[5]["transaction_date"]), '2014-12-28')
        self.assertEquals(self.format_time_struct(r[6]["transaction_date"]), '2014-12-27')

        self.assertEquals(r[0]["account_event"], "PATREON.COM")
        self.assertEquals(r[1]["account_event"], "PATREON.COM")
        self.assertEquals(r[2]["account_event"], "BURGER KING")
        self.assertEquals(r[3]["account_event"], "ICA SUPERMARKET")
        self.assertEquals(r[4]["account_event"], "ICA SUPERMARKET")
        self.assertEquals(r[5]["account_event"], "McDonalds")
        self.assertEquals(r[6]["account_event"], "SPOTIFY Spotify")

        self.assertEquals(r[0]["amount"], -8.02)
        self.assertEquals(r[1]["amount"], -7.96)
        self.assertEquals(r[2]["amount"], -69.0)
        self.assertEquals(r[3]["amount"], -93.97)
        self.assertEquals(r[4]["amount"], -88.60)
        self.assertEquals(r[5]["amount"], -75.0)
        self.assertEquals(r[6]["amount"], -49.0)

        self.assertEquals(r[0]["balance"], 6560.18)
        self.assertEquals(r[1]["balance"], 16061.26)
        self.assertEquals(r[2]["balance"], 16069.22)
        self.assertEquals(r[3]["balance"], 16138.22)
        self.assertEquals(r[4]["balance"], 16232.19)
        self.assertEquals(r[5]["balance"], 17066.54)
        self.assertEquals(r[6]["balance"], 17141.54)


    def format_time_struct(self, time_struct, format='%Y-%m-%d'):
        return time.strftime(format, time_struct)

if __name__ == '__main__':
    unittest.main()