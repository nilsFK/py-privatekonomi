#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lib.base_model import BaseModel
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
class Transaction(BaseModel):
    def __init__(self):
        self.metadata = MetaData()
        super(Transaction, self).__init__(
        Table('transaction', self.metadata,
            Column('id', Integer, primary_key = True)
        ))
