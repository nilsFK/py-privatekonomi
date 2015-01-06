#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.base_model import BaseModel
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.sql import select
class Currency(BaseModel):
    def __init__(self):
        self.metadata = MetaData()
        super(Currency, self).__init__(
            Table('currency', self.metadata,
            Column('id', Integer, primary_key = True),
            Column('code', String(3))
        ))

    def insertCode(self, code):
        result = self.execute(self.ref.insert().values(code=code))
        return result.inserted_primary_key

    def getCode(self, id):
        result = self.execute(select([self.ref.c.code]).where(self.ref.c.id==id))
        ret = result.fetchone()[0]
        result.close()
        return ret


