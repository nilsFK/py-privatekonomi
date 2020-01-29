#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, ForeignKeyConstraint
from sqlalchemy.types import Date, Numeric, DateTime

def getCustomizations(raw_models):
    customizations = {}
    customizations[raw_models['transaction_data']['type']] = {
        'ISIN' : Column('ISIN', String(128), nullable=True),
        'courtage' : Column('courtage', Numeric(precision=16, scale=2), nullable=True)
    }
    return customizations