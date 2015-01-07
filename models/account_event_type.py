#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models.base_model import BaseModel
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

class AccountEventType(BaseModel):
    def __init__(self):
        self.metadata = MetaData()
        super(AccountEventType, self).__init__(
            Table('account_event_type', self.metadata,
                Column('id', Integer, primary_key = True),
                Column('name', String(64), nullable=False)
        ))
