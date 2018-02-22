#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re
from py_privatekonomi.core.formatters.account_formatter import AccountFormatter
import py_privatekonomi.core.formatter
from py_privatekonomi.core.mappers.economy_mapper import EconomyMapper
class AvanzaFormatter(AccountFormatter):
    def __init__(self):
        super(AvanzaFormatter, self).__init__("avanza")

    @EconomyMapper("Account", "name")
    def format_account_name(self, content, subformatter):
        """ Konto: namn """
        return content.strip()

    @EconomyMapper("Transaction", "transaction_date")
    def format_transaction_transaction_date(self, content, subformatter):
        """ Transaktion: transaktionsdatum """
        return super(AvanzaFormatter, self)._format_date(content, "%Y-%m-%d")

    @EconomyMapper("Transaction", "amount")
    def format_transaction_amount(self, content, subformatter):
        """ Transaktion: belopp """
        return super(AvanzaFormatter, self)._format_currency(content)

    @EconomyMapper("TransactionType", "name")
    def format_transaction_type_name(self, content, subformatter):
        """ Transaktion: typ """
        return content.strip()

    @EconomyMapper("SecurityProvider", "name")
    def format_security_provider_name(self, content, subformatter):
        """ Värdepapper: namn """
        return content.strip()

    @EconomyMapper("Transaction", "security_amount")
    def format_transaction_security_amount(self, content, subformatter):
        """ Värdepapper: antalet """
        return super(AvanzaFormatter, self)._format_currency(content)

    @EconomyMapper("Transaction", "security_rate")
    def format_transaction_security_rate(self, content, subformatter):
        """ Värdepapper: kurs """
        return super(AvanzaFormatter, self)._format_currency(content)

    @EconomyMapper("Currency", "code")
    def format_currency_code(self, content, subformatter):
        """ Valuta: kod """
        return content.strip()

    @EconomyMapper("TransactionData", "ISIN")
    def format_transaction_data_ISIN(self, content, subformatter):
        """ Transaktionsdata: ISIN """
        if len(content) == 0:
            return None
        return content.strip()

    @EconomyMapper("TransactionData", "courtage")
    def format_transaction_data_courtage(self, content, subformatter):
        """ Transaktionsdata: Courtage """
        if content is None or content == '-':
            return None
        return super(AvanzaFormatter, self)._format_currency(content)
