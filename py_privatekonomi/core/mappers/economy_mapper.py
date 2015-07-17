#!/usr/bin/env python
# -*- coding: utf-8 -*-
from py_privatekonomi.core.error import MapperError
"""
     EconomyMapper limits decorations to known core models
     Usage outside of these core models will cause an exception
"""
class EconomyMapper(object):
    def __init__(self, model_name, model_attr = None):
        self.model_name = model_name
        self.model_attr = model_attr

    @staticmethod
    def getModelNames():
        return [
            "Account",
            "AccountCategory",
            "Currency",
            "Organization",
            "Provider",
            "SecurityProvider",
            "Transaction",
            "TransactionCategory",
            "TransactionGroup",
            "TransactionType"
        ]

    def __call__(self, formatter_func):
        def wrapper(*args):
            formatter = args[0]
            content = args[1]
            subformatter = args[2]
            model_attr = self.model_attr if (self.model_attr is not None) else subformatter
            formatted_content = formatter_func(*args)
            if self.model_name not in EconomyMapper.getModelNames():
                raise MapperError(capture_data={
                    'model_name' : self.model_name,
                    'subformatter' : model_attr,
                    'valid_model_names' : EconomyMapper.getModelNames()
                })
            formatter.addMapping(self.model_name, model_attr, formatted_content)
            return formatted_content
        return wrapper