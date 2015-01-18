#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.mapper import Mapper
import pprint
"""
     AccountMapper limits decorations to known core models
     (presently hard-coded into the constructor).
     Usage outside of these core models will cause an exception
"""
class AccountMapper(object):
    def __init__(self, model_name, model_attr = None):
        self.model_name = model_name
        self.model_attr = model_attr
        self.model_names = [
            "Account",
            "AccountCategory",
            "Currency",
            "Organization",
            "Provider",
            "Security",
            "Transaction",
            "TransactionEvent",
            "TransactionEventType"
        ]

    def __call__(self, formatter_func):
        def wrapper(*args):
            formatter = args[0]
            content = args[1]
            subformatter = args[2]
            model_attr = self.model_attr if (self.model_attr is not None) else subformatter
            formatted_content = formatter_func(*args)
            if self.model_name not in self.model_names:
                raise Exception("Invalid mapped model name: %s of subformatter `%s` (use any of %s)"
                    % (self.model_name, subformatter, repr(sorted(self.model_names))))
            formatter.addMapping(self.model_name, model_attr, formatted_content)
            return formatted_content
        return wrapper