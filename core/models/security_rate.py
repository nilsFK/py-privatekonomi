#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.models.base_model import BaseModel
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Numeric, ForeignKeyConstraint

class SecurityRate(BaseModel):
    def __init__(self, context):
        super(SecurityRate, self).__init__(
            Table('security_rate', context.metadata,
                Column('id', Integer, primary_key=True)
        ), context)
