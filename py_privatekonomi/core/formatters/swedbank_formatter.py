#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals
import sys
import re
from py_privatekonomi.core.formatters.account_formatter import AccountFormatter
import py_privatekonomi.core.formatter
from py_privatekonomi.core.formatter import Formatter
from py_privatekonomi.core.mappers.economy_mapper import EconomyMapper
class SwedbankFormatter(AccountFormatter):
    def __init__(self):
        super(SwedbankFormatter, self).__init__("swedbank")

    @EconomyMapper("Account", "account_code")
    def format_account_account_code(self, content, subformatter):
        """ Clearing-nummer """
        return content.strip().strip('"')

    @EconomyMapper("Account", "account_number")
    def format_account_account_number(self, content, subformatter):
        """ Kontonummer / Kontonr """
        return content.strip().strip('"')

    @EconomyMapper("Account", "name")
    def format_account_name(self, content, subformatter):
        """ Kontonamn """
        return content.strip().strip('"')

    @EconomyMapper("TransactionType", "name")
    def format_transaction_type_name(self, content, subformatter):
        """ Kontohändelse """
        return content.strip().strip('"')

    @EconomyMapper("Transaction", "accounting_date")
    def format_transaction_accounting_date(self, content, subformatter):
        """ Bokföringsdatum """
        content = content.strip().strip('"')
        return super(SwedbankFormatter, self)._format_date(content, None)

    @EconomyMapper("Transaction", "transaction_date")
    def format_transaction_transaction_date(self, content, subformatter):
        """ Transaktionsdatum """
        content = content.strip().strip('"')
        return super(SwedbankFormatter, self)._format_date(content, None)

    @EconomyMapper("Transaction", "reference")
    def format_transaction_reference(self, content, subformatter):
        """ Referens """
        return content.strip().strip('"')

    @EconomyMapper("Transaction", "amount")
    def format_transaction_amount(self, content, subformatter):
        """ Summa """
        return super(SwedbankFormatter, self)._format_currency(content)

    @EconomyMapper("Currency", "code")
    def format_currency_code(self, content, subformatter):
        """ Typ av valuta """
        return content.strip().strip('"')

    @EconomyMapper("Account", "current_balance")
    def format_account_current_balance(self, content, subformatter):
        """ Belopp """
        return super(SwedbankFormatter, self)._format_currency(content)
