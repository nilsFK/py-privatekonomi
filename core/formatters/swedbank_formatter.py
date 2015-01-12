#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
from core.formatters.account_formatter import AccountFormatter
import core.formatter
class SwedbankFormatter(AccountFormatter):
    def __init__(self):
        super(SwedbankFormatter, self).__init__()

    def format_accounting_date(self, content):
        """ Bokföringsdatum """
        content = content.strip()
        return super(SwedbankFormatter, self)._format_date(content, "%y-%m-%d")

    def format_transaction_date(self, content):
        """ Transaktionsdatum """
        content = content.strip()
        return super(SwedbankFormatter, self)._format_date(content, "%y-%m-%d")

    def format_account_event(self, content):
        """ Kontohändelse """
        return content.strip()

    def format_account_reference(self, content):
        """ Referens """
        return content.strip()

    def format_amount(self, content):
        """ Summa """
        return super(SwedbankFormatter, self)._format_currency(content)

    def format_balance(self, content):
        """ Belopp """
        return super(SwedbankFormatter, self)._format_currency(content)

    def format_clearing_number(self, content):
        """ Clearing-nummer """
        return content.strip()

    def format_account_number(self, content):
        """ Kontonr """
        return content.strip()

    def format_currency_code(self, content):
        """ Typ av valuta """
        return content.strip()

    def format_account_name(self, content):
        """ Kontonamn """
        return content.strip()