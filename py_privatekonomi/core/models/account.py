#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from py_privatekonomi.core.models.base_model import BaseModel
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, ForeignKeyConstraint
from sqlalchemy.types import Numeric
from collections import OrderedDict

class Account(BaseModel):
    def __init__(self, context, customizations={}):
        pre_cols = OrderedDict([
            ('id', Column('id', Integer, primary_key = True)),
            ('name', Column('name', String(255), nullable=False)),
            ('account_code', Column('account_code', String(16), nullable=False, server_default='')),
            ('account_number', Column('account_number', String(32), nullable=False, server_default='')),
            ('current_balance', Column('current_balance', Numeric(precision=16, scale=2), nullable=False, default=0.0)),
            ('future_balance', Column('future_balance', Numeric(precision=16, scale=2), nullable=True)),
            ('account_category_id', Column('account_category_id', Integer, nullable=False)),
            ('organization_id', Column('organization_id', Integer, nullable=False)),
            ('provider_id', Column('provider_id', Integer, nullable=True)),
            ('fk_account_account_category', ForeignKeyConstraint(
                ['account_category_id'],
                ['account_category.id'],
                use_alter=False,
                name='fk_account_account_category',
                onupdate='CASCADE',
                ondelete='CASCADE'
            )),
            ('fk_account_organization', ForeignKeyConstraint(
                ['organization_id'],
                ['organization.id'],
                use_alter=False,
                name='fk_account_organization',
                onupdate='CASCADE',
                ondelete='CASCADE'
            )),
            ('fk_account_provider', ForeignKeyConstraint(
                ['provider_id'],
                ['provider.id'],
                use_alter=False,
                name='fk_account_provider',
                onupdate='CASCADE',
                ondelete='CASCADE'
            ))
        ])
        # apply customizations
        for key in customizations:
            custom = customizations[key]
            pre_cols[key] = custom
        cols = list(pre_cols.values())
        super(Account, self).__init__(
            Table('account', context.metadata, *cols), context)

