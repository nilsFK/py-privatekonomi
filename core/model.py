#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy.engine import reflection
# from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, \
    update, delete, select
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

    def getName(self):
        return self.ref.name

    def generate(self):
        if db.DB().hasConfig('prefix'):
            self.ref.name = db.DB().getConfig('prefix') + "_" + self.ref.name
        self.ref.create(db.DB().getEngine(), checkfirst=True)
        return self

    def getConstraints(self):
        inspector = reflection.Inspector.from_engine(db.DB().getEngine())
        fks = []
        for fk in inspector.get_foreign_keys(self.ref.name):
            if not fk['name']:
                continue
            fks.append(ForeignKeyConstraint((), (), name=fk['name']))
        return fks

    def getForeignKeys(self, table_name):
        inspector = reflection.Inspector.from_engine(db.DB().getEngine())
        return inspector.get_foreign_keys(table_name)

    def obliterate(self):
        if not db.DB().getEngine().has_table(self.ref.name):
            return self
        # inspector = reflection.Inspector.from_engine(db.DB().getEngine())
        # fks = []
        # for fk in inspector.get_foreign_keys(self.ref.name):
        #     if not fk['name']:
        #         continue
            # fks.append(ForeignKeyConstraint((), (), name=fk['name']))

        fks = self.getConstraints()
        # t = Table(self.ref.name, MetaData(), *fks)

        for fk in fks:
            self.execute(DropConstraint(fk))

        self.ref.drop(db.DB().getEngine(), checkfirst=True)
        return self

    def col(self, val):
        return self.ref.c[val]

    def execute(self, stmt):
        return db.DB().getConnection().execute(stmt)

    def insert(self, values):
        result = db.DB().getConnection().execute(self.ref.insert().values(values))
        return result.inserted_primary_key

    # http://docs.sqlalchemy.org/en/rel_0_9/core/tutorial.html
    # http://docs.sqlalchemy.org/en/latest/core/sqlelement.html#sqlalchemy.sql.expression.ColumnElement
    def update(self, values=None, where=None):
        stmt = update(self.ref, where, values)
        result = self.execute(stmt)
        return result.rowcount

    def delete(self, where):
        if where is not None:
            stmt = delete(self.ref, where)
            result = self.execute(stmt)
            return result.rowcount
        else:
            return 0

    def select(self, columns=None, whereclause=None):
        stmt = select(columns=columns, whereclause=whereclause)
        result = self.execute(stmt)
        return result

    def selectAll(self):
        stmt = select([self.ref])
        result = self.execute(stmt)
        return result

    def selectValue(self, columns=None, whereclause=None):
        """ TODO: Implement """
        pass

    def selectOne(self, columns=None, whereclause=None):
        """ TODO: Implement """
        pass