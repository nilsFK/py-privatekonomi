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
from utilities.common import decode

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

    # Insert all items
    organization.insert([
        {
            'name' : 'Swedbank'
        },
        {
            'name' : 'Avanza'
        }
    ])

    provider.insert([
        {
            'name' : 'Collector'
        },
        {
            'name' : 'Handelsbanken'
        }
    ])

    currency.insert([
        {
            'code' : 'SEK',
            'symbol' : 'kr',
            'country' : 'SE'
        },
        {
            'code' : 'USD',
            'symbol' : '$',
            'country' : 'US'
        }
    ])

    account_category.insert([
        {
        'name' : u'Lönekonto'
        },
        {
        'name' : 'Sparkonto'
        }
    ])

    account.insert([
        {
            'name' : u'Mitt Lönekonto',
            'account_code' : '123-123',
            'account_number' : '123456789',
            'current_balance' : 12000.12,
            'future_balance' : 13000.13,
            'account_category_id' : 1,
            'organization_id' : 1,
            'provider_id' : None
        },
        {
            'name' : u'Mitt Sparkonto',
            'account_code' : '123-123',
            'account_number' : '012345678',
            'current_balance' : 2000,
            'future_balance' : None,
            'account_category_id' : 2,
            'organization_id' : 1,
            'provider_id' : 1
        }
    ])

    transaction_type.insert([
        {
            'name' : u'Insättning',
        },
        {
            'name' : u'Intjänad ränta',
        },
        {
            'name' : u'Kortköp/uttag'
        }
    ])

    transaction_category.insert([
        {
            'name' : 'Donationer'
        },
        {
            'name' : 'Matvaror'
        },
        {
            'name' : u'Fondköp'
        },
        {
            'name' : u'Fondsälj'
        }
    ])

    transaction.insert([
        {
            'group' : 1,
            'accounting_date' : '2015-01-20',
            'transaction_date' : '2015-01-20',
            'amount' : -8.02,
            'reference' : 'PATREON.COM',
            'account_id' : 1,
            'transaction_category_id' : 1,
            'transaction_type_id' : 3,
            'currency_id' : 1
        },
        {
            'group' : 1,
            'accounting_date' : '2015-01-20',
            'transaction_date' : '2015-01-20',
            'amount' : -12.00,
            'reference' : 'SPOTIFY spotify',
            'account_id' : 1,
            'transaction_category_id' : None,
            'transaction_type_id' : 3,
            'currency_id' : 1
        },
        {
            'group' : 2,
            'accounting_date' : '2015-01-20',
            'transaction_date' : '2015-01-20',
            'amount' : -100.00,
            'reference' : u'Överföring sparkonto',
            'account_id' : 1,
            'transaction_category_id' : None,
            'transaction_type_id' : 3,
            'currency_id' : 1
        },
        {
            'group' : 2,
            'accounting_date' : '2015-01-20',
            'transaction_date' : '2015-01-20',
            'amount' : 100.00,
            'reference' : u'Överföring sparkonto',
            'account_id' : 2,
            'transaction_category_id' : None,
            'transaction_type_id' : 1,
            'currency_id' : 1
        }
    ])

    # Update a few items
    transaction.update({
        'amount' : -6.66,
        'accounting_date' : '2015-01-18'
    }, transaction.col('id').in_([1,2]))

    # Delete a couple of items
    provider.delete(provider.col('id')==1)

    # Get some items
    transactions = transaction.selectAll()
    print(transactions)
    for t in transactions:
        print "id:", t[transaction.col('id')]
        print "group:", t[transaction.col('group')]
        print "accounting_date:", t[transaction.col('accounting_date')]
        print "transaction_date:", t[transaction.col('transaction_date')]
        print "amount:", t[transaction.col('amount')]
        print "reference:", decode(t[transaction.col('reference')])
        print "account_id:", t[transaction.col('account_id')]
        print "transaction_category_id:", t[transaction.col('transaction_category_id')]
        print "transaction_type_id:", t[transaction.col('transaction_type_id')]
        print "currency_id:", t[transaction.col('currency_id')]
        print "-"*80
