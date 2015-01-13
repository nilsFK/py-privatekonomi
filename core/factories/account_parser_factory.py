#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.factory import Factory

class AccountParserFactory(Factory):
    def __init__(self):
        super(AccountParserFactory, self).__init__()

    def create(self, acc_type):
        parser = self.get(acc_type)
        if parser:
            return parser()
        else:
            assert 0, ("Invalid acc_type: ", acc_type)
