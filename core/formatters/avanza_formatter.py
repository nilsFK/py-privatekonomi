#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re
from core.formatters.account_formatter import AccountFormatter
import core.formatter
from core.mappers.account_mapper import AccountMapper
class AvanzaFormatter(AccountFormatter):
    def __init__(self):
        super(AvanzaFormatter, self).__init__()

    @AccountMapper("Account")
    def format_account_name(self, content, subformatter):
        """ Konto: namn """
        return content.strip()

    @AccountMapper("Transaction")
    def format_transaction_date(self, content, subformatter):
        """ Transaktion: transaktionsdatum """
        content = content.strip()
        return super(AvanzaFormatter, self)._format_date(content, "%Y-%m-%d")

    @AccountMapper("Transaction")
    def format_transaction_amount(self, content, subformatter):
        """ Transaktion: belopp """
        return super(AvanzaFormatter, self)._format_currency(content)

    @AccountMapper("TransactionEvent")
    def format_transaction_event(self, content, subformatter):
        """ Transaktion: kontohändelse """
        return content.strip()

    @AccountMapper("Security")
    def format_security_name(self, content, subformatter):
        """ Värdepapper: namn """
        return content.strip()

    @AccountMapper("Security")
    def format_security_amount(self, content, subformatter):
        """ Värdepapper: antalet """
        return super(AvanzaFormatter, self)._format_float(content)

    @AccountMapper("Security")
    def format_security_rate(self, content, subformatter):
        """ Värdepapper: kurs """
        return super(AvanzaFormatter, self)._format_currency(content)

    @AccountMapper("Currency")
    def format_transaction_currency_code(self, content, subformatter):
        """ Valuta: kod """
        return content.strip()
