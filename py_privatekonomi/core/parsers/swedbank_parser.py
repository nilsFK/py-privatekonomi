#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import py_privatekonomi.core.parser
from py_privatekonomi.core.parsers.regex_parser import RegexParser
from py_privatekonomi.core.error import ParserError
from py_privatekonomi.utilities.common import is_string, unicode, decode
from py_privatekonomi.core.parsers.csv_parser import CsvParser
import re
import csv
import six

class SwedbankParser(py_privatekonomi.core.parser.Parser):
    def __init__(self):
        super(SwedbankParser, self).__init__("swedbank")

    def parse(self, contents, options):
        self.options = options
        ret = []
        p = re.compile(r'^\d{2}-\d{2}-\d{2}')
        for idx, content in enumerate(contents):
            if not isinstance(content, six.string_types):
                raise ParserError("Invalid transaction text content. Expected string content, instead got:", capture_data={
                    'content' : content
                })
            content = content.strip()
            content = decode(content)
            if is_string(content) and len == 0:
                continue
            elif content.startswith('* Transaktioner') and contents[idx+1].startswith("Radnummer"):
                ret = self.__parse_csv(contents[idx+2:])
                break
            elif ";" in content: # assume csv
                ret = self.__parse_legacy_csv(contents[idx:])
                break
            elif content.startswith('Clnr'):
                ret = self.__parse_clnr(contents[idx], contents[idx+1:])
                break
            elif p.match(content):
                ret = self.__parse_simple(contents[idx:])
                break
            else:
                continue
        if len(ret) == 0:
            error_msg = "Invalid transaction text content: no transactions found for text ending with: ...{suffix}".format(**{
                    'suffix' : content[-100:].strip()
                })
            raise ParserError(error_msg, capture_data={'content': content})
        return ret

    def __parse_csv(self, contents):
        """
            This applies to the new csv export of Swedbank.
        """
        subformatters = [
            None, # Radnummer
            "account_account_code",
            "account_account_number",
            None, # Produkt
            "currency_code",
            "transaction_accounting_date",
            "transaction_transaction_date",
            None, # Valutadag
            "transaction_reference",
            None, # Beskrivning
            "transaction_amount",
            "account_current_balance"
        ]
        print(("Filetype:", self.options['filetype']))
        if self.options['filetype'] in ['csv', 'empty']:
            opts = {
                'delimiter' : str(','),
                'quoting' : csv.QUOTE_NONE
            }
            rows = CsvParser().parse(contents, opts=opts)
            return (rows, subformatters)
        else:
            return (contents, subformatters)

    def __parse_legacy_csv(self, contents):
        """
            This parser triggers when old csv export is used.
        """
        subformatters = [
            "transaction_reference",
            "transaction_transaction_date",
            "transaction_amount",
            "account_current_balance"
        ]
        if self.options['filetype'] in ['csv', 'empty']:
            opts = {
                'delimiter' : str(';'),
                'quoting' : csv.QUOTE_NONE
            }
            rows = CsvParser().parse(contents, opts=opts)
            return (rows, subformatters)
        else:
            return (contents, subformatters)


    def __parse_clnr(self, headers, contents):
        """
        Notice: this applies to the old version of Swedbank.
        This parser triggers when old text export
        Note that we have to find all the UNICODE characters, not just the regular
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
            "account_account_code",
            "account_account_number",
            "account_name",
            "currency_code",
            "transaction_accounting_date",
            "transaction_transaction_date",
            "transaction_reference",
            "transaction_type_name",
            "transaction_amount"
        ]
        return (results, subformatters)

    def __parse_simple(self, contents):
        """
            Notice: this applies to the old version of Swedbank.
            This parser triggers on manual copy and paste from old website.
        """
        regex_parser = RegexParser()
        parsed = regex_parser.parse(contents, r'\s{2,}|\t+')
        subformatters = [
            "transaction_accounting_date",
            "transaction_transaction_date",
            "transaction_reference",
            "transaction_amount",
            "account_current_balance"
        ]
        return (parsed, subformatters)