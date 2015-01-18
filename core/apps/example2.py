#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.models.account import Account
from core.models.account_category import AccountCategory
from core.models.transaction_event import TransactionEvent
from core.models.transaction_event_type import TransactionEventType
from core.models.currency import Currency
from core.models.organization import Organization
from core.models.provider import Provider
from core.models.transaction import Transaction

import core.db
from utilities import helper, common
from sqlalchemy import MetaData
from core.model_context import ModelContext

def execute(sources, parser, formatter):
    contents = helper.execute(sources, parser, formatter, True)
    for content in contents:
        print content
    return content

def persist(output):
    core.db.DB().connect()
    context = ModelContext()

    transaction = Transaction(context).obliterate()
    account = Account(context).obliterate()
    account_category = AccountCategory(context).obliterate().generate()
    transaction_event = TransactionEvent(context).obliterate().generate()
    transaction_event_type = TransactionEventType(context).obliterate().generate()
    currency = Currency(context).obliterate().generate()
    organization = Organization(context).obliterate().generate()
    provider = Provider(context).obliterate().generate()
    account.generate()
    transaction.generate()

    id1 = currency.insertCurrency(code="SEK",symbol="kr",country="SE")
    id2 = currency.insertCurrency(code="USD",symbol="$",country="US")
    code = currency.getCode(id1[0])
    print(id1)
    print(id2)
    print(code)