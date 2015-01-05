#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
import db
class Model(object):
    def __init__(self):
        self.metadata = MetaData()
    def create(self):
        self.metadata.create_all(db.DB().getEngine())