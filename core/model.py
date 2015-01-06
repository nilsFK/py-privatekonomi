#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
import db
class Model(object):
    def __init__(self):
        pass

    def generate(self):
        self.metadata.create_all(db.DB().getEngine())
        return self

    def getRef(self):
        return self.ref

    def obliterate(self):
        self.ref.drop(db.DB().getEngine(), checkfirst=True)
        return self

    def execute(self, stmt):
        return db.DB().getConnection().execute(stmt)
