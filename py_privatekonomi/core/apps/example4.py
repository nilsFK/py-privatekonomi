#!/usr/bin/env python
# -*- coding: utf-8 -*-

import core.db
from core.mappers.economy_mapper import EconomyMapper
from utilities import helper
from utilities.models import rebuild_tables, create_tables
from core.persisters.economy_persist import EconomyPersist
from py_privatekonomi.core import loader
from utilities.common import as_obj
import sys

"""
    An extension of example3.py that does not rebuild tables, but
    create tables from scratch (if necessary).
    If there is any data in the database we fill those data gaps
    that need to be sealed.
"""

def execute(sources, parser, formatter, configs):
    contents = helper.execute(sources, parser, formatter, True) # <--
    return contents

def persist(output, configs):
    models = create_tables(loader.load_models(EconomyMapper.getModelNames()))
    for content in output:
        __persist(content, models, configs)

def __persist(content, models, configs):
    economy_persist = EconomyPersist(models, configs.insert_rows)
    economy_persist.useLogging(configs.use_logging)
    save_output_to_file = configs.log_to_file

    #########################################
    # PROVIDER
    # =======================================
    provider = models.Provider.get()
    economy_persist.fillDataGap(models.Provider,
        models.Provider.getResults(provider, ['id', 'name']))

    #########################################
    # ACCOUNT CATEGORY
    # =======================================
    account_category = models.AccountCategory.get()
    economy_persist.fillDataGap(models.AccountCategory,
        models.AccountCategory.getResults(account_category, ['id', 'name']))

    #########################################
    # ORGANIZATION
    # =======================================
    organization = models.Organization.get()
    economy_persist.fillDataGap(models.Organization,
        models.Organization.getResults(organization, ['id', 'name']))

    #########################################
    # ACCOUNT
    # =======================================
    account = models.Account.get()
    economy_persist.fillDataGap(models.Account,
        models.Account.getResults(account, ['id', 'name']))

    #########################################
    # TRANSACTION CATEGORY
    # =======================================
    transaction_category = models.TransactionCategory.get()
    economy_persist.fillDataGap(models.TransactionCategory,
        models.TransactionCategory.getResults(transaction_category, ['id', 'name']))

    #########################################
    # CURRENCY
    # =======================================
    currency = models.Currency.get()
    economy_persist.fillDataGap(models.Currency,
        models.Currency.getResults(currency, ['id', 'code', 'symbol', 'country']))


    #########################################
    # TRANSACTION TYPE
    # =======================================
    transaction_type = models.TransactionType.get()
    economy_persist.fillDataGap(models.TransactionType,
        models.TransactionType.getResults(transaction_type, ['id', 'name']))

    #########################################
    # SECURITY RATE
    # =======================================
    security_rate = models.SecurityRate.get()
    economy_persist.fillDataGap(models.SecurityRate,
        models.SecurityRate.getResults(security_rate, ['id']))

    if save_output_to_file is not False:
        orig_stdout = sys.stdout
        f = file(save_output_to_file, "w")
        sys.stdout = f

    economy_persist.persist(content)

    if save_output_to_file is not False:
        sys.stdout = orig_stdout
        f.close()
