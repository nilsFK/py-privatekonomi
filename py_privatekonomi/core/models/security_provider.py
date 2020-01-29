#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from py_privatekonomi.core.models.base_model import BaseModel
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Numeric, ForeignKeyConstraint
from collections import OrderedDict

class SecurityProvider(BaseModel):
    def __init__(self, context, customizations={}):
        pre_cols = OrderedDict([
            ('id', Column('id', Integer, primary_key = True)),
            ('name', Column('name', String(255), nullable=False)),
            ('security_type', Column('security_type', String(64), nullable=True))
        ])
        # apply customizations
        for key in customizations:
            custom = customizations[key]
            pre_cols[key] = custom
        cols = list(pre_cols.values())
        super(SecurityProvider, self).__init__(
            Table('security_provider', context.metadata, *cols), context)
