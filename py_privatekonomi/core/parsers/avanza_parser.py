#!/usr/bin/env python
# -*- coding: utf-8 -*-
import py_privatekonomi.core.parser
import re
import csv
from py_privatekonomi.core.parsers.csv_parser import CsvParser

class AvanzaParser(py_privatekonomi.core.parser.Parser):
    def __init__(self):
        pass

    def parse(self, contents):
        # skip headers
        contents = contents[1:]

        opts = {
            'delimiter' : ';',
            'quoting' : csv.QUOTE_NONE
        }
        rows = CsvParser().parse(contents, opts=opts)
        subformatters = [
            "transaction_transaction_date",
            "account_name",
            "transaction_type_name",
            "security_name",
            "security_rate_amount",
            "security_rate_rate",
            "transaction_amount",
            "currency_code"
        ]
        return (rows, subformatters)