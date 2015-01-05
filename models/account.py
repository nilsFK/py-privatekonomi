#!/usr/bin/env python
# -*- coding: utf-8 -*-
from base_model import BaseModel
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
class Account(BaseModel):
    def __init__(self):
        super(Account, self).__init__()
        ref = Table('account', self.metadata,
            Column('id', Integer, primary_key = True)
        )
