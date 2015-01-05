#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lib.base_model import BaseModel
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
class Currency(BaseModel):
    def __init__(self):
        self.metadata = MetaData()
        super(Currency, self).__init__(
            Table('currency', self.metadata,
            Column('id', Integer, primary_key = True)
        ))
