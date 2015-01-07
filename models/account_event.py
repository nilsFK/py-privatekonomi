#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models.base_model import BaseModel
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

class AccountEvent(BaseModel):
    def __init__(self, context):
        super(AccountEvent, self).__init__(
            Table('account_event', context.metadata,
                Column('id', Integer, primary_key = True),
                Column('event', String(32), nullable = False)
        ), context)
