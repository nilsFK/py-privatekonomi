#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from py_privatekonomi.core.models.base_model import BaseModel
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Numeric, ForeignKeyConstraint

class Security(BaseModel):
    def __init__(self, context):
        super(Security, self).__init__(
            Table('security', context.metadata,
                Column('id', Integer, primary_key=True),
                Column('rate', Numeric(precision=16, scale=2), nullable=False),
                Column('amount', Numeric(precision=16, scale=4), nullable=False),
                # Column('transaction_id', Integer, nullable=False),
                Column('security_provider_id', Integer, nullable=False),
                # ForeignKeyConstraint(
                #     ['transaction_id'],
                #     ['transaction.id'],
                #     use_alter=False,
                #     name='fk_security_transaction',
                #     onupdate='CASCADE',
                #     ondelete='CASCADE'
                # ),
                ForeignKeyConstraint(
                    ['security_provider_id'],
                    ['security_provider.id'],
                    use_alter=False,
                    name='fk_security_security_provider',
                    onupdate='CASCADE',
                    ondelete='CASCADE'
                )
        ), context)
