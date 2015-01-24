#!/usr/bin/env python
# -*- coding: utf-8 -*-
import core.db
from core.models.account import Account
from core.models.account_category import AccountCategory
from core.models.transaction_category import TransactionCategory
from core.models.transaction_type import TransactionType
from core.models.currency import Currency
from core.models.organization import Organization
from core.models.provider import Provider
from core.models.transaction import Transaction
from core.models.security import Security
from core.mappers.account_mapper import AccountMapper
from utilities.common import decode
from utilities import resolver

from utilities import helper, common
from sqlalchemy import MetaData
from core.model_context import ModelContext
import loader

def __get_models():
    context = ModelContext()

    # fetch models
    models = loader.load_models(AccountMapper.getModelNames())
    model_type_mappings = dict((k, v["type"]) for k,v in models.iteritems())
    model_types = model_type_mappings.values()
    model_deps = resolver.getModelDependencies(model_types)

    # obliterate tables
    obliteration_order = resolver.resolveObliteration(model_deps)
    for obliterate in obliteration_order:
        model = model_type_mappings[obliterate]
        model(context).obliterate()

    # generate tables
    generation_order = resolver.resolveGeneration(model_deps)
    context = ModelContext()
    generated_models = {}
    for generate in generation_order:
        model = model_type_mappings[generate]
        generated_models[generate] = model(context).generate()
    return generated_models

def execute(sources, parser, formatter):
    contents = helper.execute(sources, parser, formatter, True)
    for content in contents:
        print content
    return content

def persist(output):
    core.db.DB().connect()

    models = __get_models()

    # Insert all items
    models['organization'].insert([
        {
            'name' : 'Swedbank'
        },
        {
            'name' : 'Avanza'
        }
    ])

    models['provider'].insert([
        {
            'name' : 'Collector'
        },
        {
            'name' : 'Handelsbanken'
        }
    ])

    models['currency'].insert([
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

    models['account_category'].insert([
        {
        'name' : u'Lönekonto'
        },
        {
        'name' : 'Sparkonto'
        }
    ])

    models['account'].insert([
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

    models['transaction_type'].insert([
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

    models['transaction_category'].insert([
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

    models['transaction'].insert([
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
    models['transaction'].update({
        'amount' : -6.66,
        'accounting_date' : '2015-01-18'
    }, models['transaction'].col('id').in_([1,2]))

    # Delete a couple of items
    models['provider'].delete(models['provider'].col('id')==1)

    # Get some items
    transactions = models['transaction'].selectAll()
    for t in transactions:
        print "id:", t[models['transaction'].col('id')]
        print "group:", t[models['transaction'].col('group')]
        print "accounting_date:", t[models['transaction'].col('accounting_date')]
        print "transaction_date:", t[models['transaction'].col('transaction_date')]
        print "amount:", t[models['transaction'].col('amount')]
        print "reference:", decode(t[models['transaction'].col('reference')])
        print "account_id:", t[models['transaction'].col('account_id')]
        print "transaction_category_id:", t[models['transaction'].col('transaction_category_id')]
        print "transaction_type_id:", t[models['transaction'].col('transaction_type_id')]
        print "currency_id:", t[models['transaction'].col('currency_id')]
        print "-"*80
