#!/usr/bin/env python
# -*- coding: utf-8 -*-
from py_privatekonomi.core.models.base_model import BaseModel
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, ForeignKeyConstraint
from sqlalchemy.types import Date, Numeric, DateTime
from collections import OrderedDict

class Transaction(BaseModel):
    def __init__(self, context, customizations={}):
        pre_cols = OrderedDict([
            ('id', Column('id', Integer, primary_key=True)),
            ('group', Column('group', Integer, nullable=False, index=True)),
            ('accounting_date', Column('accounting_date', Date, nullable=True)),
            ('transaction_date', Column('transaction_date', Date, nullable=False)),
            ('amount', Column('amount', Numeric(precision=16, scale=2), nullable=False)),
            ('reference', Column('reference', String(512), nullable=False, server_default='')),
            ('created', Column('created', DateTime, nullable=False)),
            ('security_rate', Column('security_rate', Numeric(precision=16, scale=2), nullable=True)),
            ('security_amount', Column('security_amount', Numeric(precision=16, scale=4), nullable=True)),
            ('account_id', Column('account_id', Integer, nullable=False)),
            ('transaction_category_id', Column('transaction_category_id', Integer, nullable=True)),
            ('transaction_type_id', Column('transaction_type_id', Integer, nullable=False)),
            ('currency_id', Column('currency_id', Integer, nullable=False)),
            ('security_provider_id', Column('security_provider_id', Integer, nullable=True)),
            ('fk_transaction_account', ForeignKeyConstraint(
                ['account_id'],
                ['account.id'],
                use_alter=False,
                name='fk_transaction_account',
                onupdate='CASCADE',
                ondelete='CASCADE'
                )),
            ('fk_transaction_transaction_type', ForeignKeyConstraint(
                ['transaction_type_id'],
                ['transaction_type.id'],
                use_alter=False,
                name='fk_transaction_transaction_type',
                onupdate='CASCADE',
                ondelete='CASCADE'
                )),
            ('fk_transaction_transaction_category', ForeignKeyConstraint(
                    ['transaction_category_id'],
                    ['transaction_category.id'],
                    use_alter=False,
                    name='fk_transaction_transaction_category',
                    onupdate='CASCADE',
                    ondelete='CASCADE'
                )),
            ('fk_transaction_currency', ForeignKeyConstraint(
                    ['currency_id'],
                    ['currency.id'],
                    use_alter=False,
                    name='fk_transaction_currency',
                    onupdate='CASCADE',
                    ondelete='CASCADE'
                )),
            ('fk_transaction_security_provider', ForeignKeyConstraint(
                    ['security_provider_id'],
                    ['security_provider.id'],
                    use_alter=False,
                    name='fk_transaction_security_provider',
                    onupdate='CASCADE',
                    ondelete='CASCADE'
                ))
        ])
        # apply customizations
        for key in customizations:
            custom = customizations[key]
            pre_cols[key] = custom
        cols = pre_cols.values()
        super(Transaction, self).__init__(
            Table('transaction', context.metadata, *cols), context)