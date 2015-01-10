#!/usr/bin/env python
# -*- coding: utf-8 -*-
import formatters.swedbank_formatter
from core.factory import Factory

class AccountFormatterFactory(Factory):
    def __init__(self):
        super(AccountFormatterFactory, self).__init__({
            'swedbank' : formatters.swedbank_formatter.SwedbankFormatter
        })

    def createAccountFormatter(self, acc_type, formatters):
        formatter = self.get(acc_type)
        if formatter:
            return formatter(formatters)
        else:
            assert 0, ("Invalid acc_type: ", acc_type)
