#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from py_privatekonomi.core.mappers.economy_mapper import EconomyMapper
from py_privatekonomi.utilities import helper
from py_privatekonomi.utilities.common import decode
from py_privatekonomi.utilities import resolver
from py_privatekonomi.utilities.models import rebuild_tables
from py_privatekonomi.utilities import helper, common
from py_privatekonomi.core import loader
from sqlalchemy import desc, asc

"""
    This app extends the functionality of example1.py
    by adding another function: persist(), which is the
    main ground to persist output data to the database.
    Note that we are all ready connected to the database
    when we enter the persist function and the only thing
    we have to bother about is how to insert that data to
    the database.
"""

def execute(sources, parser, formatter, configs):
    contents = helper.execute(sources, parser, formatter, False)
    for content in contents:
        print(content)
    return content

def persist(output, configs):
    models = rebuild_tables(loader.load_models(EconomyMapper.getModelNames()))

    # Insert all items
    models.Organization.insert([
        {
            'name' : 'Swedbank'
        },
        {
            'name' : 'Avanza'
        }
    ])

    models.Provider.insert([
        {
            'name' : 'Collector'
        },
        {
            'name' : 'Handelsbanken'
        }
    ])

    models.Currency.insert([
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

    models.AccountCategory.insert([
        {
        'name' : 'Lönekonto'
        },
        {
        'name' : 'Sparkonto'
        }
    ])

    models.Account.insert([
        {
            'name' : 'Mitt Lönekonto',
            'account_code' : '123-123',
            'account_number' : '123456789',
            'current_balance' : 12000.12,
            'future_balance' : 13000.13,
            'account_category_id' : 1,
            'organization_id' : 1,
            'provider_id' : None
        },
        {
            'name' : 'Mitt Sparkonto',
            'account_code' : '123-123',
            'account_number' : '012345678',
            'current_balance' : 2000,
            'future_balance' : None,
            'account_category_id' : 2,
            'organization_id' : 1,
            'provider_id' : 1
        }
    ])

    models.TransactionType.insert([
        {
            'name' : 'Insättning',
        },
        {
            'name' : 'Intjänad ränta',
        },
        {
            'name' : 'Kortköp/uttag'
        }
    ])

    models.TransactionCategory.insert([
        {
            'name' : 'Donationer'
        },
        {
            'name' : 'Matvaror'
        },
        {
            'name' : 'Fondköp'
        },
        {
            'name' : 'Fondsälj'
        }
    ])

    models.Transaction.insert([
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
            'reference' : 'Överföring sparkonto',
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
            'reference' : 'Överföring sparkonto',
            'account_id' : 2,
            'transaction_category_id' : None,
            'transaction_type_id' : 1,
            'currency_id' : 1
        }
    ])

    # Update a few items
    models.Transaction.update({
        'amount' : -6.66,
        'accounting_date' : '2015-01-18'
    }, models.Transaction.col('id').in_([1,2]))

    # Delete a couple of items
    models.Provider.delete(models.Provider.col('id')==1)

    # Get some items
    transactions = models.Transaction.selectAll()
    for t in transactions:
        print(("id:", t[models.Transaction.col('id')]))
        print(("group:", t[models.Transaction.col('group')]))
        print(("accounting_date:", t[models.Transaction.col('accounting_date')]))
        print(("transaction_date:", t[models.Transaction.col('transaction_date')]))
        print(("amount:", t[models.Transaction.col('amount')]))
        print(("reference:", decode(t[models.Transaction.col('reference')])))
        print(("account_id:", t[models.Transaction.col('account_id')]))
        print(("transaction_category_id:", t[models.Transaction.col('transaction_category_id')]))
        print(("transaction_type_id:", t[models.Transaction.col('transaction_type_id')]))
        print(("currency_id:", t[models.Transaction.col('currency_id')]))
        print(("-"*80))

    # Get some items and order them descending/ascending
    stmt = models.Transaction.getSelectStatement(models.Transaction.cols(['id', 'accounting_date'])).order_by(desc(models.Transaction.c().accounting_date))
    transactions = models.Transaction.execute(stmt)
    print("transactions ordered by accounting date descending")
    for t in transactions:
        print(("id:", t[models.Transaction.col('id')]))
        print(("accounting date:", t[models.Transaction.col('accounting_date')]))
    print(("-"*80))
    stmt = models.Transaction.getSelectStatement(models.Transaction.cols(['id', 'accounting_date'])).order_by(asc(models.Transaction.c().accounting_date))
    transactions = models.Transaction.execute(stmt)
    print("transactions ordered by accounting date ascending")
    for t in transactions:
        print(("id:", t[models.Transaction.col('id')]))
        print(("accounting date:", t[models.Transaction.col('accounting_date')]))
