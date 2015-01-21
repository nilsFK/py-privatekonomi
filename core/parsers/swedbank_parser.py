#!/usr/bin/env python
# -*- coding: utf-8 -*-

import core.parser
import re
from core.parsers.regex_parser import RegexParser
from core.error import ParserError

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
                ret = self.__parse_clnr(contents[idx], contents[idx+1:])
                break
            elif p.match(content):
                ret = self.__parse_simple(contents[idx:])
                break
            else:
                continue
        if len(ret) == 0:
            raise ParserError("Invalid transaction text content: no transactions found for text ending with: %s" % content[0:100].strip() + "...")
        return ret

    def __parse_clnr(self, headers, contents):
        """Note that we have to find all the UNICODE characters, not just the regular
        A-Z0-9, so make sure to pass re.UNICODE to fetch these. Also, we try to decode
        from utf-8 if in that format, in case of fail we just pass it as is.
        """
        try:
            headers = re.findall(r'(\w+\s*)', headers.decode('utf-8'), re.UNICODE)
        except:
            headers = re.findall(r'(\w+\s*)', headers, re.UNICODE)
        header_lengths = [len(x) for x in headers]
        header_offsets = [sum( list( header_lengths[:header[0]+1] ) ) for header in enumerate(headers)]
        results = []
        for content in contents:
            if len(content.strip()) == 0:
                continue
            result = []
            for idx, current_offset in enumerate(header_offsets):
                previous_offset = header_offsets[idx-1] if idx > 0 else 0
                """There is an issue with regards to how the headers align with the values;
                the values can expand over their respective boundaries, we have to manage
                the last two headers below (see last_pieces).
                """
                if idx >= 7: break
                token = content[previous_offset : current_offset]
                result.append(token)
            last_pieces = content[header_offsets[idx-1]:].strip()
            result.extend(re.split(r'\s{2,}', last_pieces))
            results.append(result)
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
        return (results, subformatters)

    def __parse_simple(self, contents):
        regex_parser = RegexParser()
        parsed = regex_parser.parse(contents, r'\t+')
        subformatters = [
            "accounting_date",
            "transaction_date",
            "account_reference",
            "amount",
            "balance"
        ]
        return (parsed, subformatters)