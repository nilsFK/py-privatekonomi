#!/usr/bin/env python
# -*- coding: utf-8 -*-

import core.parser
import re
from core.parsers.regex_parser import RegexParser

class SwedbankParser(core.parser.Parser):
    def __init__(self):
        pass

    def parse(self, contents):
        ret = []
        p = re.compile(r'^\d{2}-\d{2}-\d{2}')
        for idx, content in enumerate(contents):
            content = content.strip()
            if content == '':
                continue
            elif content.startswith('Clnr'):
                ret = self.__parse_clnr(contents[idx+1:])
                break
            elif p.match(content):
                ret = self.__parse_simple(contents[idx:])
                break
            else:
                continue
        return ret

    def __parse_clnr(self, contents):
        regex_parser = RegexParser()
        parsed = regex_parser.parse(contents, r'\s{2,}')
        subformatters = [
            "clearing_number",
            "account_number",
            "account_name",
            "currency_code",
            "accounting_date",
            "transaction_date",
            "account_reference",
            "account_event",
            "amount"
        ]
        return (parsed, subformatters)

    def __parse_simple(self, contents):
        regex_parser = RegexParser()
        parsed = regex_parser.parse(contents, r'\t+')
        formatters = [
            "accounting_date",
            "transaction_date",
            "account_reference",
            "amount",
            "balance"
        ]
        return (parsed, formatters)