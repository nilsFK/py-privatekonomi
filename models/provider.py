#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.base_model import BaseModel
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

class Provider(BaseModel):
    def __init__(self):
        self.metadata = MetaData()
        super(Provider, self).__init__(
            Table('provider', self.metadata,
                Column('id', Integer, primary_key = True),
                Column('name', String(128), nullable=False)
        ))
