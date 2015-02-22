#!/usr/bin/env python
# -*- coding: utf-8 -*-

import core.db
from core.mappers.account_mapper import AccountMapper
from utilities import helper
from utilities.models import rebuild_tables
from utilities import helper
from core.persisters.account_persist import AccountPersist
import loader
import sys

"""
    Notice that we pass True to helper.execute as the last argument.
    This will transform the contents into data that is formatted
    according to how it maps to the models. This is very useful
    for saving data to the database since it enables automatization
    using the core.persist.Persist class.
"""

def execute(sources, parser, formatter):
    contents = helper.execute(sources, parser, formatter, True) # <--
    return contents

def persist(output):
    models = rebuild_tables(loader.load_models(AccountMapper.getModelNames()))
    for content in output:
        __persist(content, models)

def __persist(content, models):
    account_persist = AccountPersist(models)
    account_persist.useLogging(True)
    # Set to False to disable or path to file to enable
    save_output_to_file = True
    save_output_to_file = "C:\\out.txt"
    # account_persist.buffer(models.Transaction, 100)
    # account_persist.buffer(models.Security, 100)

    #########################################
    # PROVIDER
    # =======================================
    provider = models.Provider.createAndGet({
        'name' : 'Collector'
    }, 'id')
    account_persist.fillDataGap(models.Provider,
        models.Provider.getResults(
            provider, ['id', 'name']
    )[0])


    #########################################
    # ACCOUNT CATEGORY
    # =======================================
    account_category = models.AccountCategory.createAndGet({
        'name' : u'Okänd'
    }, 'id')
    account_persist.fillDataGap(models.AccountCategory,
        models.AccountCategory.getResults(
            account_category, ['id', 'name']
    )[0])


    #########################################
    # ORGANIZATION
    # =======================================
    organization = models.Organization.createAndGet({
        'name' : 'Swedbank'
    }, 'id')
    account_persist.fillDataGap(models.Organization,
        models.Organization.getResults(
            organization, ['id', 'name']
    )[0])


    #########################################
    # ACCOUNT
    # =======================================
    account = models.Account.createAndGet({
        'name' : u'Okänd',
        'account_category_id' : models.AccountCategory.id(),
        'organization_id' : models.Organization.id(),
        'account_code' : '123-456',
        'account_number' : '1234567890',
        'current_balance' : 12345.67
    }, 'id')
    account_persist.fillDataGap(models.Account,
        models.Account.getResults(
            account, ['id', 'name']
    )[0])


    #########################################
    # TRANSACTION CATEGORY
    # =======================================
    transaction_category = models.TransactionCategory.createAndGet({
        'name' : u'Okänd'
    }, 'id')
    account_persist.fillDataGap(models.TransactionCategory,
        models.TransactionCategory.getResults(
            transaction_category, ['id', 'name']
    )[0])


    #########################################
    # CURRENCY
    # =======================================
    currency_sek = models.Currency.createAndGet({
        'code' : 'SEK',
        'symbol' : 'kr',
        'country' : 'SE'
    }, 'id')
    currency_usd = models.Currency.createAndGet({
        'code' : 'USD',
        'symbol' : '$',
        'country' : 'US'
    }, 'id')
    account_persist.fillDataGap(models.Currency,
        models.Currency.getResults(
            currency_sek, ['id', 'code', 'symbol', 'country']
    )[0])
    account_persist.fillDataGap(models.Currency,
        models.Currency.getResults(
            currency_usd, ['id', 'code', 'symbol', 'country']
    )[0])


    #########################################
    # TRANSACTION TYPE
    # =======================================
    transaction_type = models.TransactionType.createAndGet({
        'name' : u'Okänd'
    }, 'id')
    account_persist.fillDataGap(models.TransactionType,
        models.TransactionType.getResults(
            transaction_type, ['id', 'name']
    )[0])


    if save_output_to_file is not False:
        orig_stdout = sys.stdout
        f = file(save_output_to_file, "w")
        sys.stdout = f

    account_persist.persist(content)

    if save_output_to_file:
        sys.stdout = orig_stdout
        f.close()
