#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models.base_model import BaseModel
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.types import Numeric
class Account(BaseModel):
    def __init__(self):
        self.metadata = MetaData()
        super(Account, self).__init__(
            Table('account', self.metadata,
                Column('id', Integer, primary_key = True),
                Column('name', String(255), nullable=False),
                Column('account_code', String(16), nullable=False),
                Column('account_number', String(32), nullable=False),
                Column('current_balance', Numeric(precision=16, scale=2),
                    nullable=False),
                Column('future_balance', Numeric(precision=16, scale=2),
                    nullable=True)
        ))
