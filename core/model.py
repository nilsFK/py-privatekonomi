#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy.engine import reflection
# from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.schema import (
    MetaData,
    Table,
    DropTable,
    ForeignKeyConstraint,
    DropConstraint
)
import db
class Model(object):
    def __init__(self, context):
        self.context = context

    def getRef(self):
        return self.ref

    def getMetadata(self):
        return self.context.metadata

    def generate(self):
        self.ref.create(db.DB().getEngine(), checkfirst=True)
        return self

    def obliterate(self):
        if not db.DB().getEngine().has_table(self.ref.name):
            return self
        inspector = reflection.Inspector.from_engine(db.DB().getEngine())
        fks = []
        for fk in inspector.get_foreign_keys(self.ref.name):
            if not fk['name']:
                continue
            fks.append(ForeignKeyConstraint((), (), name=fk['name']))
        t = Table(self.ref.name, MetaData(), *fks)

        for fk in fks:
            self.execute(DropConstraint(fk))

        self.ref.drop(db.DB().getEngine(), checkfirst=True)
        return self

    def execute(self, stmt):
        return db.DB().getConnection().execute(stmt)
