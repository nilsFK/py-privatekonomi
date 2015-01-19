#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.models.base_model import BaseModel
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, ForeignKeyConstraint

class TransactionCategory(BaseModel):
    def __init__(self, context):
        super(TransactionCategory, self).__init__(
            Table('transaction_category', context.metadata,
                Column('id', Integer, primary_key=True),
                Column('name', String(128), nullable=False)
        ), context)
