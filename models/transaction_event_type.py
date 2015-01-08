#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models.base_model import BaseModel
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

class TransactionEventType(BaseModel):
    def __init__(self, context):
        super(TransactionEventType, self).__init__(
            Table('transaction_event_type', context.metadata,
                Column('id', Integer, primary_key = True),
                Column('name', String(64), nullable=False)
        ), context)
