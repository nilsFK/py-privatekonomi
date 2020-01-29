#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
import py_privatekonomi.core.parser
import re
import csv
from py_privatekonomi.core.parsers.csv_parser import CsvParser

class AvanzaParser(py_privatekonomi.core.parser.Parser):
    def __init__(self):
        super(AvanzaParser, self).__init__("avanza")

    def parse(self, contents, options):
        # skip headers
        contents = contents[1:]
        subformatters = [
            "transaction_transaction_date",
            "account_name",
            "transaction_type_name",
            "security_provider_name",
            "transaction_security_amount",
            "transaction_security_rate",
            "transaction_amount",
            "transaction_data_courtage",
            "currency_code",
            "transaction_data_ISIN"
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

