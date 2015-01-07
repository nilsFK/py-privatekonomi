#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models.base_model import BaseModel
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

class AccountCategory(BaseModel):
    def __init__(self):
        self.metadata = MetaData()
        super(AccountCategory, self).__init__(
            Table('account_category', self.metadata,
                Column('id', Integer, primary_key = True),
                Column('name', String(32), nullable=False)
        ))
