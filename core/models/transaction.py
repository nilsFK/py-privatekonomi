#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.models.base_model import BaseModel
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, ForeignKeyConstraint
from sqlalchemy.types import Date, Numeric, DateTime

class Transaction(BaseModel):
    def __init__(self, context):
        super(Transaction, self).__init__(
            Table('transaction', context.metadata,
                Column('id', Integer, primary_key=True),
                Column('group', Integer, nullable=False, index=True),
                Column('accounting_date', Date, nullable=True),
                Column('transaction_date', Date, nullable=False),
                Column('amount', Numeric(precision=16, scale=2), nullable=False),
                Column('reference', String(512), nullable=False),
                Column('created', DateTime, nullable=False),
                Column('account_id', Integer, nullable=False),
                Column('transaction_category_id', Integer, nullable=True),
                Column('transaction_type_id', Integer, nullable=False),
                Column('currency_id', Integer, nullable=False),
                ForeignKeyConstraint(
                    ['account_id'],
                    ['account.id'],
                    use_alter=False,
                    name='fk_transaction_account',
                    onupdate='CASCADE',
                    ondelete='CASCADE'
                ),
                ForeignKeyConstraint(
                    ['transaction_type_id'],
                    ['transaction_type.id'],
                    use_alter=False,
                    name='fk_transaction_transaction_type',
                    onupdate='CASCADE',
                    ondelete='CASCADE'
                ),
                ForeignKeyConstraint(
                    ['transaction_category_id'],
                    ['transaction_category.id'],
                    use_alter=False,
                    name='fk_transaction_transaction_category',
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

