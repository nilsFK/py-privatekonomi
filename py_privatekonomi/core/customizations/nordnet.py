#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, ForeignKeyConstraint
from sqlalchemy.types import Date, Numeric, DateTime

def getCustomizations(raw_models):
    customizations = {}
    customizations[raw_models['transaction_data']['type']] = {
        'identifier' : Column('identifier', String(128), nullable=True),
        'liquidity_date' : Column('liquidity_date', Date, nullable=True),
        'type' : Column('type', String(128), nullable=True),
        'ISIN' : Column('ISIN', String(128), nullable=True),
        'interest' : Column('interest', Numeric(precision=16, scale=2), nullable=True),
        'fee' : Column('fee', Numeric(precision=16, scale=2), nullable=True),
        'purchase_value' : Column('purchase_value', Numeric(precision=16, scale=2), nullable=True),
        'results' : Column('results', Numeric(precision=16, scale=2), nullable=True),
        'total_amount' : Column('total_amount', Numeric(precision=16, scale=2), nullable=True),
        'exchange_rate' : Column('exchange_rate', Numeric(precision=16, scale=2), nullable=True),
        'transaction_text' : Column('transaction_text', String(256), nullable=True),
        'cancellation_date' : Column('cancellation_date', Date, nullable=True),
        'verification_no' : Column('verification_no', String(256), nullable=True)
    }
    return customizations