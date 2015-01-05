#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
class Migrate(object):
    def __init__(self):
        self.metadata = MetaData()

    def migrate():
