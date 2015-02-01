#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.models.base_model import BaseModel
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.sql import select

class Currency(BaseModel):
    def __init__(self, context):
        super(Currency, self).__init__(
            Table('currency', context.metadata,
                Column('id', Integer, primary_key=True),
                Column('code', String(3), nullable=False, unique=True),
                Column('symbol', String(3), nullable=False),
                Column('country', String(64), nullable=False)
        ), context)

