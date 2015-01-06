#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.base_model import BaseModel
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

class Organization(BaseModel):
    def __init__(self):
        self.metadata = MetaData()
        super(Organization, self).__init__(
            Table('organization', self.metadata,
                Column('id', Integer, primary_key = True),
                Column('name', String(128), nullable=False)
        ))
