#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.models.base_model import BaseModel
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

class Security(BaseModel):
    def __init__(self, context):
        super(Security, self).__init__(
            Table('security', context.metadata,
                Column('id', Integer, primary_key = True),
                Column('rate', Numeric(precision=16, scale=2), nullable=False),
                Column('amount', Numeric(precision=16, scale=4), nullable=False)
        ), context)