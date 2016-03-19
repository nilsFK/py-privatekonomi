#!/usr/bin/env python
# -*- coding: utf-8 -*-
from py_privatekonomi.core.models.base_model import BaseModel
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, ForeignKeyConstraint
from sqlalchemy.types import Date, Numeric, DateTime
from collections import OrderedDict

class TransactionData(BaseModel):
    """
    Any additional transaction data should be stored in this model.
    This model should be customized with additional fields with transaction
    data that is not stored in the transaction model and is a rare piece of data, such as ISIN-numbers, cancellation dates, etc.
    """
    def __init__(self, context, customizations={}):
        pre_cols = OrderedDict([
            ('id', Column('id', Integer, primary_key=True)),
        ])
        # apply customizations
        for key in customizations:
            custom = customizations[key]
            pre_cols[key] = custom
        cols = pre_cols.values()
        super(TransactionData, self).__init__(
            Table('transaction_data', context.metadata, *cols), context)