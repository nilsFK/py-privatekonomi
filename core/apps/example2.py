#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.models.account import Account
from core.models.account_category import AccountCategory
from core.models.transaction_category import TransactionCategory
from core.models.transaction_type import TransactionType
from core.models.currency import Currency
from core.models.organization import Organization
from core.models.provider import Provider
from core.models.transaction import Transaction
from core.models.security import Security

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

    security = Security(context).obliterate()
    transaction = Transaction(context).obliterate()
    account = Account(context).obliterate()
    account_category = AccountCategory(context).obliterate().generate()
    transaction_category = TransactionCategory(context).obliterate()
    transaction_type = TransactionType(context).obliterate().generate()
    transaction_category.generate()
    currency = Currency(context).obliterate().generate()
    organization = Organization(context).obliterate().generate()
    provider = Provider(context).obliterate().generate()
    account.generate()
    transaction.generate()
    security.generate()

    id1 = currency.insertCurrency(code="SEK",symbol="kr",country="SE")
    id2 = currency.insertCurrency(code="USD",symbol="$",country="US")
    code = currency.getCode(id1[0])
    print(id1)
    print(id2)
    print(code)