#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from py_privatekonomi.core.models.base_model import BaseModel
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

class Provider(BaseModel):
    def __init__(self, context):
        super(Provider, self).__init__(
            Table('provider', context.metadata,
                Column('id', Integer, primary_key=True),
                Column('name', String(128), nullable=False, unique=True)
        ), context)
