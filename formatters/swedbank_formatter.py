#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Formats input to a data structure according to the
# input acquired from Swedbank transactions
import sys
import lib.formatter
class SwedbankFormatter(lib.formatter.Formatter):
    def __init__(self):
        lib.formatter.Formatter.formatters = [
            "accounting_date",
            "transaction_date",
            "account_event",
            "amount",
            "balance"
        ]

    @classmethod
    def format_accounting_date(self, content):
        content = content.strip()
        return super(SwedbankFormatter, self).format_date(content, "%y-%m-%d")

    @classmethod
    def format_transaction_date(self, content):
        content = content.strip()
        return super(SwedbankFormatter, self).format_date(content, "%y-%m-%d")

    @classmethod
    def format_account_event(self, content):
        return content.strip()

    @classmethod
    def format_amount(self, content):
        return super(SwedbankFormatter, self).format_currency(content)

    @classmethod
    def format_balance(self, content):
        return super(SwedbankFormatter, self).format_currency(content)
