#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from py_privatekonomi.core.models.base_model import BaseModel
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

class TransactionGroup(BaseModel):
    def __init__(self, context):
        super(TransactionGroup, self).__init__(
            Table('transaction_group', context.metadata,
                Column('id', Integer, primary_key=True)
        ), context)

    def allocate(self):
        """ allocates and returns transaction_group id. """
        try: # sqlalchemy 3.x
            tg_id = self.insert(None)[0]
        except Exception as e: # sqlalchemy 4.x
            tg_id = self.insert({})[0]
        return tg_id
