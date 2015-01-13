#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.models.base_model import BaseModel
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, ForeignKeyConstraint
from sqlalchemy.types import Date, Numeric

class Transaction(BaseModel):
    def __init__(self, context):
        super(Transaction, self).__init__(
            Table('transaction', context.metadata,
                Column('id', Integer, primary_key = True),
                Column('account_id', Integer),
                Column('transaction_event_id', Integer),
                Column('currency_id', Integer),
                Column('accounting_date', Date, nullable=False),
                Column('transaction_date', Date, nullable=True),
                Column('balance', Numeric(precision=16, scale=2), nullable=False),
                Column('amount', Numeric(precision=2, scale=2), nullable=False),
                ForeignKeyConstraint(
                    ['account_id'],
                    ['account.id'],
                    use_alter=False,
                    name='fk_transaction_account',
                    onupdate='CASCADE',
                    ondelete='CASCADE'
                ),
                ForeignKeyConstraint(
                    ['transaction_event_id'],
                    ['transaction_event.id'],
                    use_alter=False,
                    name='fk_transaction_transaction_event',
                    onupdate='CASCADE',
                    ondelete='CASCADE'
                ),
                ForeignKeyConstraint(
                    ['currency_id'],
                    ['currency.id'],
                    use_alter=False,
                    name='fk_transaction_currency',
                    onupdate='CASCADE',
                    ondelete='CASCADE'
                ),
            ), context)
