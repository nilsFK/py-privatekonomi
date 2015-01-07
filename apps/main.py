#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from models.account import Account
from models.account_category import AccountCategory
from models.account_event import AccountEvent
from models.account_event_type import AccountEventType
from models.currency import Currency
from models.organization import Organization
from models.provider import Provider
from models.transaction import Transaction

import core.db
from utilities import helper
from sqlalchemy import MetaData
from core.model_context import ModelContext

def execute(source, parser, formatter):
    content = helper.read_file(source)

    parser = helper.get_parser(parser)
    parsed = parser.parse(content, r'\t+')

    formatter = helper.get_formatter(formatter)
    return formatter.format(parsed)

def persist(output):
    core.db.DB().connect()
    context = ModelContext()
    transaction = Transaction(context).obliterate()
    account = Account(context).obliterate().generate()
    transaction.generate()
    account_category = AccountCategory(context).obliterate().generate()
    account_event = AccountEvent(context).obliterate().generate()
    account_event_type = AccountEventType(context).obliterate().generate()
    currency = Currency(context).obliterate().generate()
    organization = Organization(context).obliterate().generate()
    provider = Provider(context).obliterate().generate()

    id1 = currency.insertCurrency(code="SEK",symbol="kr",country="SE")
    id2 = currency.insertCurrency(code="USD",symbol="$",country="US")
    code = currency.getCode(id1[0])
    print(id1)
    print(id2)
    print(code)