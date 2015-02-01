#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy.engine import reflection
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, \
    update, delete, select
from sqlalchemy.schema import (
    MetaData,
    Table,
    DropTable,
    ForeignKeyConstraint,
    DropConstraint
)
import re
import db
from utilities.models import get_model_name

class Model(object):
    def __init__(self, context):
            self.context = context

    def getRef(self):
        return self.ref

    def getMetadata(self):
        return self.context.metadata

    def getName(self):
        return self.ref.name

    def getNormalizedName(self):
        return self.__normalized_name

    def generate(self):
        if db.DB().hasConfig('prefix'):
            self.__prefix = db.DB().getConfig('prefix')
            self.__normalized_name = self.ref.name
            self.ref.name = self.__prefix + "_" + self.ref.name
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

    def getDependencies(self):
        ret = []
        fks = self.ref.foreign_keys
        for fk in fks:
            str_ref = vars(fk)["_colspec"]
            contents = re.match("(.*)\.(.*)", str_ref)
            str_ref_table = contents.group(1)
            str_ref_col = contents.group(2)
            ret.append({
                'reference' : str_ref,
                'referenced_table' : str_ref_table,
                'referenced_model' : get_model_name(str_ref_table),
                'referenced_col' : str_ref_col,
                'referencing_col' : vars(vars(fk)["parent"])["key"]
            })
        return ret


    def getForeignKeys(self, table_name):
        if not db.DB().getEngine().has_table(self.ref.name):
            return []
        inspector = reflection.Inspector.from_engine(db.DB().getEngine())
        return inspector.get_foreign_keys(table_name)

    def obliterate(self):
        if db.DB().hasConfig('prefix'):
            self.ref.name = db.DB().getConfig('prefix') + "_" + self.ref.name
        if not db.DB().getEngine().has_table(self.ref.name):
            return self

        fks = self.getConstraints()
        Table(self.ref.name, MetaData(), *fks)
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

    def selectValue(self, column, whereclause=None):
        result = self.selectOne([self.col(column)], whereclause)
        for res in result:
            return res[self.col(column)]
        else:
            return False
        return False

    def selectOne(self, columns=None, whereclause=None):
        stmt = select(columns=columns, whereclause=whereclause).limit(1)
        result = self.execute(stmt)
        return result

    def existsBy(self, by_col, by_val):
        select_value = self.selectValue(by_col, self.col(by_col) == by_val)
        return select_value is not False
