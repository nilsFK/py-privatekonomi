#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re
from core.formatters.account_formatter import AccountFormatter
import core.formatter
from core.mappers.economy_mapper import EconomyMapper
class AvanzaFormatter(AccountFormatter):
    def __init__(self):
        super(AvanzaFormatter, self).__init__()

    @EconomyMapper("Account", "name")
    def format_account_name(self, content, subformatter):
        """ Konto: namn """
        return content.strip()

    @EconomyMapper("Transaction", "transaction_date")
    def format_transaction_date(self, content, subformatter):
        """ Transaktion: transaktionsdatum """
        content = content.strip()
        return super(AvanzaFormatter, self)._format_date(content, "%Y-%m-%d")

    @EconomyMapper("Transaction", "amount")
    def format_transaction_amount(self, content, subformatter):
        """ Transaktion: belopp """
        return super(AvanzaFormatter, self)._format_currency(content)

    @EconomyMapper("TransactionType", "name")
    def format_transaction_event(self, content, subformatter):
        """ Transaktion: typ """
        return content.strip()

    @EconomyMapper("Security", "name")
    def format_security_name(self, content, subformatter):
        """ Värdepapper: namn """
        return content.strip()

    @EconomyMapper("SecurityRate", "amount")
    def format_security_amount(self, content, subformatter):
        """ Värdepapper: antalet """
        return super(AvanzaFormatter, self)._format_float(content)

    @EconomyMapper("SecurityRate", "rate")
    def format_security_rate(self, content, subformatter):
        """ Värdepapper: kurs """
        return super(AvanzaFormatter, self)._format_currency(content)

    @EconomyMapper("Currency", "code")
    def format_transaction_currency_code(self, content, subformatter):
        """ Valuta: kod """
        return content.strip()
