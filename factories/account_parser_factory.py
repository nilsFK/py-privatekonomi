#!/usr/bin/env python
# -*- coding: utf-8 -*-
import parsers

class AccountParserFactory(object):
    def __init__(self):
        self.parsers = {
            'whitespace' : parsers.ws_parser.WhitespaceParser
        }

    def createAccountParser(self, acc_type):
        if acc_type not in self.parsers.keys():
            assert 0, ("Invalid acc_type: ", acc_type)
        return self.parsers[acc_type]()