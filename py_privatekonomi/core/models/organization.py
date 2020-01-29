#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from py_privatekonomi.core.models.base_model import BaseModel
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

class Organization(BaseModel):
    def __init__(self, context):
        super(Organization, self).__init__(
            Table('organization', context.metadata,
                Column('id', Integer, primary_key=True),
                Column('name', String(128), nullable=False, unique=True)
        ), context)
