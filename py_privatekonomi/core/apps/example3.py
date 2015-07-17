#!/usr/bin/env python
# -*- coding: utf-8 -*-

import py_privatekonomi.core.db
from py_privatekonomi.core.mappers.economy_mapper import EconomyMapper
from py_privatekonomi.utilities import helper
from py_privatekonomi.utilities.models import rebuild_tables, create_tables
from py_privatekonomi.core import loader
import sys
from py_privatekonomi.utilities.common import as_obj
from py_privatekonomi.core.transaction import (TransactionManager, Transaction, CustomTransaction, TransactionHelper)

"""
    Notice that we pass True to helper.execute as the last argument.
    This will transform the contents into data that is formatted
    according to how it maps to the models. This is very useful
    for saving data to the database since it enables automatization
    using core.transaction
"""

def execute(sources, parser, formatter, configs):
    contents = helper.execute(sources, parser, formatter, True) # <--
    # print(contents)
    return contents

def persist(output, configs):
    models = rebuild_tables(loader.load_models(EconomyMapper.getModelNames()))
    ids = {}
    ids['account_category_id'] = models.AccountCategory.create({
        'name' : 'Unknown account category'
    })
    ids['organization_id'] = models.Organization.create({
        'name' : 'Unknown organization'
    })
    ids['account_id'] = models.Account.create({
        'name' : 'Unknown account',
        'account_code' : '123-456',
        'account_number' : '1234567890',
        'account_category_id' : ids['account_category_id'],
        'organization_id' : ids['organization_id']
        })
    ids['transaction_category_id'] = models.TransactionCategory.create({
        'name' : 'Unknown transaction category'
    })
    ids['transaction_type_id'] = models.TransactionType.create({
        'name' : 'Unknown transaction type'
    })
    ids['currency_id'] = models.Currency.create({
        'code' : '?',
        'symbol' : '?',
        'country' : '?'
    })
    for content in output:
        __persist(content, models, configs, ids)

def __persist(transactions, models, configs, ids):
    transaction_manager = TransactionManager(models.Transaction, configs.insert_rows)
    transaction_group = TransactionHelper.createTransactionGroup(models)
    save_output_to_file = configs.log_to_file

    if save_output_to_file is not False:
        orig_stdout = sys.stdout
        f = file(save_output_to_file, "w")
        sys.stdout = f

    for transaction in transactions:
        t = CustomTransaction(transaction, transaction_group, models)
        t.setDefault('account_id', ids['account_id'])
        t.setDefault('transaction_category_id', ids['transaction_category_id'])
        t.setDefault('transaction_type_id', ids['transaction_type_id'])
        t.setDefault('currency_id', ids['currency_id'])
        t.setDefault('account_category_id', ids['account_category_id'])
        t.setDefault('organization_id', ids['organization_id'])
        t.setDefault('security_provider_id', None)
        t.buildTransaction()
        transaction_manager.addTransaction(t.getTransaction())
        transaction_manager.debuffer()
    transaction_manager.forceDebuffer()
    if save_output_to_file is not False:
        sys.stdout = orig_stdout
        f.close()
