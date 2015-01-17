#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re
from core.formatters.account_formatter import AccountFormatter
import core.formatter
class AvanzaFormatter(AccountFormatter):
    def __init__(self):
        super(AvanzaFormatter, self).__init__()

    def format_transaction_date(self, content):
        """ Transaktion: transaktionsdatum """
        content = content.strip()
        return super(AvanzaFormatter, self)._format_date(content, "%Y-%m-%d")

    def format_account_name(self, content):
        """ Konto: namn """
        return content.strip()

    def format_transaction_event(self, content):
        """ Transaktion: kontohändelse """
        return content.strip()

    def format_security_name(self, content):
        """ Värdepapper: namn """
        return content.strip()

    def format_security_amount(self, content):
        """ Värdepapper: antalet """
        return super(AvanzaFormatter, self)._format_float(content)

    def format_security_rate(self, content):
        """ Värdepapper: kurs """
        return super(AvanzaFormatter, self)._format_currency(content)

    def format_transaction_amount(self, content):
        """ Transaktion: belopp """
        return super(AvanzaFormatter, self)._format_currency(content)

    def format_transaction_currency_code(self, content):
        """ Valuta: kod """
        return content.strip()

