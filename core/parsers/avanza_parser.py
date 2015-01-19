#!/usr/bin/env python
# -*- coding: utf-8 -*-
import core.parser
import re
import csv
from core.parsers.csv_parser import CsvParser

class AvanzaParser(core.parser.Parser):
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
            "transaction_date",
            "account_name",
            "transaction_event",
            "security_name",
            "security_amount",
            "security_rate",
            "transaction_amount",
            "transaction_currency_code"
        ]
        return (rows, subformatters)