#!/usr/bin/env python
# -*- coding: utf-8 -*-
import parsers.regex_parser
import parsers.swedbank_parser
from core.factory import Factory

class AccountParserFactory(Factory):
    def __init__(self):
        super(AccountParserFactory, self).__init__({
            'regex' : parsers.regex_parser.RegexParser,
            'swedbank' : parsers.swedbank_parser.SwedbankParser
        })

    def createAccountParser(self, acc_type):
        parser = self.get(acc_type)
        if parser:
            return parser()
        else:
            assert 0, ("Invalid acc_type: ", acc_type)
