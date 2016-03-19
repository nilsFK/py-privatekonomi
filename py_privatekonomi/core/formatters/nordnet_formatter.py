#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re
from py_privatekonomi.core.formatters.account_formatter import AccountFormatter
import py_privatekonomi.core.formatter
from py_privatekonomi.core.mappers.economy_mapper import EconomyMapper
import numbers
class NordnetFormatter(AccountFormatter):
    def __init__(self):
        super(NordnetFormatter, self).__init__("nordnet")

    @EconomyMapper("TransactionData", "identifier")
    def format_transaction_data_identifier(self, content, subformatter):
        """ Transaktionsdata: unik identifierare """
        if isinstance(content, numbers.Real):
            return str(int(content))
        else:
            return content.strip()

    @EconomyMapper("Transaction", "accounting_date")
    def format_transaction_accounting_date(self, content, subformatter):
        """ Transaktion: bokföringsdatum """
        return super(NordnetFormatter, self)._format_date(content, "%Y-%m-%d")

    @EconomyMapper("Transaction", "transaction_date")
    def format_transaction_transaction_date(self, content, subformatter):
        """ Transaktion: transaktionsdatum """
        return super(NordnetFormatter, self)._format_date(content, "%Y-%m-%d")

    @EconomyMapper("TransactionData", "liquidity_date")
    def format_transaction_data_liquidity_date(self, content, subformatter):
        """ Transaktionsdata: likviditetsdag """
        return super(NordnetFormatter, self)._format_date(content, "%Y-%m-%d")

    @EconomyMapper("TransactionType", "name")
    def format_transaction_type_name(self, content, subformatter):
        """ Transaktion: typ """
        return content.strip()

    @EconomyMapper("SecurityProvider", "name")
    def format_security_provider_name(self, content, subformatter):
        """ SecurityProvider: namn """
        return content.strip()

    @EconomyMapper("TransactionData", "type")
    def format_transaction_data_type(self, content, subformatter):
        """ Transaktionsdata: typ """
        if len(content) == 0:
            return None
        return content.strip()

    @EconomyMapper("TransactionData", "ISIN")
    def format_transaction_data_ISIN(self, content, subformatter):
        """ Transaktionsdata: ISIN """
        if len(content) == 0:
            return None
        return content.strip()

    @EconomyMapper("Transaction", "security_amount")
    def format_transaction_security_amount(self, content, subformatter):
        """ Värdepapper: antalet """
        return super(NordnetFormatter, self)._format_currency(content)

    @EconomyMapper("Transaction", "security_rate")
    def format_transaction_security_rate(self, content, subformatter):
        """ Värdepapper: kurs """
        return super(NordnetFormatter, self)._format_currency(content)

    @EconomyMapper("TransactionData", "interest")
    def format_transaction_data_interest(self, content, subformatter):
        """ Transaktionsdata: ränta """
        return super(NordnetFormatter, self)._format_currency(content)

    @EconomyMapper("TransactionData", "fee")
    def format_transaction_data_fee(self, content, subformatter):
        """ Transaktionsdata: avgifter/courtage (?) """
        return super(NordnetFormatter, self)._format_currency(content)

    @EconomyMapper("Transaction", "amount")
    def format_transaction_amount(self, content, subformatter):
        """ Transaktion: belopp """
        return super(NordnetFormatter, self)._format_currency(content)

    @EconomyMapper("Currency", "code")
    def format_currency_code(self, content, subformatter):
        """ Valuta: kod """
        return content.strip()

    @EconomyMapper("TransactionData", "purchase_value")
    def format_transaction_data_purchase_value(self, content, subformatter):
        """ Transaktionsdata: Inköpsvärde """
        return super(NordnetFormatter, self)._format_currency(content)

    @EconomyMapper("TransactionData", "results")
    def format_transaction_data_results(self, content, subformatter):
        """ Transaktionsdata: resultat (?) """
        return super(NordnetFormatter, self)._format_currency(content)

    @EconomyMapper("TransactionData", "total_amount")
    def format_transaction_data_total_amount(self, content, subformatter):
        """ Transaktionsdata: total """
        return super(NordnetFormatter, self)._format_currency(content)

    @EconomyMapper("Account", "current_balance")
    def format_account_current_balance(self, content, subformatter):
        """ Konto: nuvarande balans """
        return super(NordnetFormatter, self)._format_currency(content)

    @EconomyMapper("TransactionData", "exchange_rate")
    def format_transaction_data_exchange_rate(self, content, subformatter):
        """ Transaktionsdata: växlingskurs """
        return super(NordnetFormatter, self)._format_currency(content)

    @EconomyMapper("TransactionData", "transaction_text")
    def format_transaction_data_transaction_text(self, content, subformatter):
        """ Transaktionsdata: transaktionstext """
        if len(content) == 0:
            return None
        return content.strip()

    @EconomyMapper("TransactionData", "cancellation_date")
    def format_transaction_data_cancellation_date(self, content, subformatter):
        """ Transaktionsdata: makuleringsdatum """
        if len(content) == 0:
            return None
        return super(NordnetFormatter, self)._format_date(content, "%Y-%m-%d")

    @EconomyMapper("TransactionData", "verification_no")
    def format_transaction_data_verification_no(self, content, subformatter):
        """ Transaktionsdata: verifikations-/notanummer """
        if isinstance(content, numbers.Real):
            return str(int(content))
        else:
            return content.strip()