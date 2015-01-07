#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models.base_model import BaseModel
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.types import Date, Numeric
class Transaction(BaseModel):
    def __init__(self):
        self.metadata = MetaData()
        super(Transaction, self).__init__(
            Table('transaction', self.metadata,
                Column('id', Integer, primary_key = True),
                Column('accounting_date', Date, nullable=False),
                Column('transaction_date', Date, nullable=True),
                Column('balance', Numeric(precision=16, scale=2), nullable=False),
                Column('amount', Numeric(precision=2, scale=2), nullable=False)
            ))
