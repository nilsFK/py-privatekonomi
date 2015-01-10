#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import formatters.account_formatter
import core.formatter
class SwedbankFormatter(formatters.account_formatter.AccountFormatter):
    def __init__(self):
        # pass
        core.formatter.Formatter.formatters = [
            "accounting_date",
            "transaction_date",
            "account_event",
            "amount",
            "balance"
        ]

    @classmethod
    def format_accounting_date(self, content):
        """ Bokföringsdatum """
        content = content.strip()
        return super(SwedbankFormatter, self)._format_date(content, "%y-%m-%d")

    @classmethod
    def format_transaction_date(self, content):
        """ Transaktionsdatum """
        content = content.strip()
        return super(SwedbankFormatter, self)._format_date(content, "%y-%m-%d")

    @classmethod
    def format_account_event(self, content):
        """ Kontohändelse """
        return content.strip()

    @classmethod
    def format_account_reference(self, content):
        """ Referens """
        return content.strip()

    @classmethod
    def format_amount(self, content):
        """ Summa """
        return super(SwedbankFormatter, self)._format_currency(content)

    @classmethod
    def format_balance(self, content):
        """ Belopp """
        return super(SwedbankFormatter, self)._format_currency(content)

    @classmethod
    def format_clearing_number(self, content):
        """ Clnr """
        return content.strip()

    @classmethod
    def format_account_number(self, content):
        """ Kontonr """
        return content.strip()

    @classmethod
    def format_currency(self, content):
        """ Valuta """
        return content.strip()