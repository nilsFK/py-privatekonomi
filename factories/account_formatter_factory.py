#!/usr/bin/env python
# -*- coding: utf-8 -*-
import formatters

class AccountFormatterFactory(object):
    def __init__(self):
        self.formatters = {
            'swedbank' : formatters.swedbank_formatter.SwedbankFormatter
        }

    def createAccountFormatter(self, acc_type):
        if acc_type not in self.formatters.keys():
            assert 0, ("Invalid acc_type: ", acc_type)
        return self.formatters[acc_type]()