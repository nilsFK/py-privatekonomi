#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
import db
class Model(object):
    def __init__(self):
        pass

    def generate(self):
        self.metadata.create_all(db.DB().getEngine())
        return self.ref

    def getRef(self):
        return self.ref