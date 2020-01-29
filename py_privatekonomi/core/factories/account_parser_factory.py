#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from py_privatekonomi.core.factory import Factory

class AccountParserFactory(Factory):
    def __init__(self):
        super(AccountParserFactory, self).__init__()

    def create(self, acc_type):
        parser = self.get(acc_type)
        if parser:
            return parser()
        else:
            return None
