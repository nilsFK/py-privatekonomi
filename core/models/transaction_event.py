#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.models.base_model import BaseModel
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

class TransactionEvent(BaseModel):
    def __init__(self, context):
        super(TransactionEvent, self).__init__(
            Table('transaction_event', context.metadata,
                Column('id', Integer, primary_key = True),
                Column('event', String(32), nullable = False)
        ), context)
