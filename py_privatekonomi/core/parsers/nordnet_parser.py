#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
import py_privatekonomi.core.parser
import re
import csv
from py_privatekonomi.core.parsers.csv_parser import CsvParser

class NordnetParser(py_privatekonomi.core.parser.Parser):
    def __init__(self):
        super(NordnetParser, self).__init__("nordnet")

    def parse(self, contents, options):
        # skip headers
        contents = contents[1:]
        subformatters = [
            "transaction_data_identifier",
            "transaction_accounting_date",
            "transaction_transaction_date",
            "transaction_data_liquidity_date",
            "transaction_type_name",
            "security_provider_name",
            "transaction_data_type",
            "transaction_data_ISIN",
            "transaction_security_amount",
            "transaction_security_rate",
            "transaction_data_interest",
            "transaction_data_fee",
            "transaction_amount",
            "currency_code",
            "transaction_data_purchase_value",
            "transaction_data_results",
            "transaction_data_total_amount",
            "account_current_balance",
            "transaction_data_exchange_rate",
            "transaction_data_transaction_text",
            "transaction_data_cancellation_date",
            "transaction_data_verification_no",
        ]
        if options['filetype'] in ['csv', 'empty']:
            opts = {
                'delimiter' : str(';'),
                'quoting' : csv.QUOTE_NONE
            }
            rows = CsvParser().parse(contents, opts=opts)
            return (rows, subformatters)
        else:
            return (contents, subformatters)

