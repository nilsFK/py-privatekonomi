#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.factory import Factory

class AccountFormatterFactory(Factory):
    def __init__(self):
        super(AccountFormatterFactory, self).__init__()

    def create(self, acc_type):
        formatter = self.get(acc_type)
        if formatter:
            return formatter()
        else:
            assert 0, ("Invalid acc_type: ", acc_type)
