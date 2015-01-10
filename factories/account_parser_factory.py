#!/usr/bin/env python
# -*- coding: utf-8 -*-
import parsers.regex_parser
import parsers.swedbank_parser

class AccountParserFactory(object):
    def __init__(self):
        self.parsers = {
            'regex' : parsers.regex_parser.RegexParser,
            'swedbank' : parsers.swedbank_parser.SwedbankParser
        }

    def createAccountParser(self, acc_type):
        if acc_type not in self.parsers.keys():
            assert 0, ("Invalid acc_type: ", acc_type)
        return self.parsers[acc_type]()

    def getTypes():
        return self.parsers.keys()