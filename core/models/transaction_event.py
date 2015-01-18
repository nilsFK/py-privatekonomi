#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.models.base_model import BaseModel
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, ForeignKeyConstraint

class TransactionEvent(BaseModel):
    def __init__(self, context):
        super(TransactionEvent, self).__init__(
            Table('transaction_event', context.metadata,
                Column('id', Integer, primary_key = True),
                Column('event', String(32), nullable = False),
                Column('transaction_event_type_id', Integer),
                ForeignKeyConstraint(
                    ['transaction_event_type_id'],
                    ['transaction_event_type.id'],
                    use_alter=False,
                    name='fk_transaction_event_transaction_event_type',
                    onupdate='CASCADE',
                    ondelete='CASCADE'
                )
        ), context)
