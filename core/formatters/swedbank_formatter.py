#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
from core.formatters.account_formatter import AccountFormatter
import core.formatter
from core.formatter import Formatter
from core.mappers.economy_mapper import EconomyMapper
class SwedbankFormatter(AccountFormatter):
    def __init__(self):
        super(SwedbankFormatter, self).__init__()

    @EconomyMapper("Account", "account_code")
    def format_clearing_number(self, content, subformatter):
        """ Clearing-nummer """
        return content.strip()

    @EconomyMapper("Account", "account_number")
    def format_account_number(self, content, subformatter):
        """ Kontonr """
        return content.strip()

    @EconomyMapper("Account", "name")
    def format_account_name(self, content, subformatter):
        """ Kontonamn """
        return content.strip()

    @EconomyMapper("TransactionType", "name")
    def format_account_event(self, content, subformatter):
        """ Kontohändelse """
        return content.strip()

    @EconomyMapper("Transaction", "accounting_date")
    def format_accounting_date(self, content, subformatter):
        """ Bokföringsdatum """
        content = content.strip()
        return super(SwedbankFormatter, self)._format_date(content, "%y-%m-%d")

    @EconomyMapper("Transaction", "transaction_date")
    def format_transaction_date(self, content, subformatter):
        """ Transaktionsdatum """
        content = content.strip()
        return super(SwedbankFormatter, self)._format_date(content, "%y-%m-%d")

    @EconomyMapper("Transaction", "reference")
    def format_account_reference(self, content, subformatter):
        """ Referens """
        return content.strip()

    @EconomyMapper("Transaction", "amount")
    def format_amount(self, content, subformatter):
        """ Summa """
        return super(SwedbankFormatter, self)._format_currency(content)

    def format_balance(self, content, subformatter):
        """ Belopp """
        return super(SwedbankFormatter, self)._format_currency(content)

    @EconomyMapper("Currency", "code")
    def format_currency_code(self, content, subformatter):
        """ Typ av valuta """
        return content.strip()

