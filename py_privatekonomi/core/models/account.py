#!/usr/bin/env python
# -*- coding: utf-8 -*-
from py_privatekonomi.core.models.base_model import BaseModel
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, ForeignKeyConstraint
from sqlalchemy.types import Numeric
class Account(BaseModel):
    def __init__(self, context):
        super(Account, self).__init__(
            Table('account', context.metadata,
                Column('id', Integer, primary_key = True),
                Column('name', String(255), nullable=False),
                Column('account_code', String(16), nullable=False, server_default=''),
                Column('account_number', String(32), nullable=False, server_default=''),
                Column('current_balance', Numeric(precision=16, scale=2), nullable=False, default=0.0),
                Column('future_balance', Numeric(precision=16, scale=2), nullable=True),
                Column('account_category_id', Integer, nullable=False),
                Column('organization_id', Integer, nullable=False),
                Column('provider_id', Integer, nullable=True),
                ForeignKeyConstraint(
                    ['account_category_id'],
                    ['account_category.id'],
                    use_alter=False,
                    name='fk_account_account_category',
                    onupdate='CASCADE',
                    ondelete='CASCADE'
                ),
                ForeignKeyConstraint(
                    ['organization_id'],
                    ['organization.id'],
                    use_alter=False,
                    name='fk_account_organization',
                    onupdate='CASCADE',
                    ondelete='CASCADE'
                ),
                ForeignKeyConstraint(
                    ['provider_id'],
                    ['provider.id'],
                    use_alter=False,
                    name='fk_account_provider',
                    onupdate='CASCADE',
                    ondelete='CASCADE'
                ),
        ), context)
