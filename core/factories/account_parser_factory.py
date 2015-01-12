#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from core.parsers import regex_parser
# from core.parsers import swedbank_parser
from core.factory import Factory

class AccountParserFactory(Factory):
    def __init__(self):
        super(AccountParserFactory, self).__init__()
        # super(AccountParserFactory, self).__init__({
        #     'regex' : regex_parser.RegexParser,
        #     'swedbank' : swedbank_parser.SwedbankParser
        # })

    def create(self, acc_type):
        parser = self.get(acc_type)
        if parser:
            return parser()
        else:
            assert 0, ("Invalid acc_type: ", acc_type)
