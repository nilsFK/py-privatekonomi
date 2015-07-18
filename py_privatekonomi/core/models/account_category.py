#!/usr/bin/env python
# -*- coding: utf-8 -*-
from py_privatekonomi.core.models.base_model import BaseModel
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from collections import OrderedDict

class AccountCategory(BaseModel):
    def __init__(self, context, customizations={}):
        pre_cols = OrderedDict([
            ('id', Column('id', Integer, primary_key=True)),
            ('name', Column('name', String(128), nullable=False, unique=True))
        ])
        # apply customizations
        for key in customizations:
            custom = customizations[key]
            pre_cols[key] = custom
        cols = pre_cols.values()
        super(AccountCategory, self).__init__(
            Table('account_category', context.metadata, *cols), context)
