#!/usr/bin/env python
# -*- coding: utf-8 -*-

import core.db
from core.mappers.account_mapper import AccountMapper
from utilities import helper
from utilities.common import decode
from utilities import resolver
from utilities.models import rebuild_tables, get_dependency_order
from utilities import helper, common
from utilities import models as models_utility
import loader
import sys

"""
    Notice that we pass True to helper.execute as the last argument.
    This will transform the contents into data that is formatted
    according to how it maps to the models. This is very useful
    for saving data to the database and will enable the automatization
    of inserting data into the database.
"""

def execute(sources, parser, formatter):
    contents = helper.execute(sources, parser, formatter, True) # <--
    return contents

def persist(output):
    models = rebuild_tables(AccountMapper.getModelNames())
    for content in output:
        __persist(content, models)

def __persist(content, models):
    dependency_order = get_dependency_order(models)
    generated_data = {}
    for model in dependency_order:
        generated_data[model] = []
    for data in content:
        generated = []
        resolved_dependencies_data = {}
        for idx, model in enumerate(dependency_order):
            model_data = data[model] if model in data else None
            generated = __call_func(models, model, model_data, resolved_dependencies_data)
            generated_data[model].append(generated)
            resolved_dependencies_data[model] = generated

def __call_func(models, model_name, model_data, resolved_dependencies_data):
    func_name = "__manage_%(table_name)s" % {
        'table_name' : models_utility.get_table_name(model_name)
    }
    res = getattr(sys.modules[__name__], func_name)(models, model_data, resolved_dependencies_data)
    return res

def __manage_account(models, account_data, resolved_dependencies_data):
    account_id = None
    if account_data is None:
        account_data = {}
        account_data["name"] = u"Okänd"
    has_account = models.Account.existsBy("name", account_data["name"])
    if has_account is False:
        account_data.update({
            'account_category_id' : resolved_dependencies_data["AccountCategory"],
            'organization_id' : resolved_dependencies_data["Organization"]
        })
        if resolved_dependencies_data["Provider"]:
            account_data.update({
                'provider_id' : resolved_dependencies_data["Provider"]
            })
        if "account_number" not in account_data:
            account_data["account_number"] = ""
        if "account_code" not in account_data:
            account_data["account_code"] = ""
        account_id = models.Account.create(account_data)
    if account_id is None:
        account_id = models.Account.getValue('id', 'name', account_data["name"])
    return account_id

def __manage_transaction_type(models, transaction_type_data, resolved_dependencies_data):
    transaction_type_id = None
    if transaction_type_data is None:
        name = u"Okänd"
    else:
        name = transaction_type_data["name"]
    has_transaction_type = models.TransactionType.existsBy("name", name)
    if has_transaction_type is False:
        transaction_type_id = models.TransactionType.create({
            "name" : name
        })
    if transaction_type_id is None:
        transaction_type_id = models.TransactionType.getValue('id', 'name', name)
    return transaction_type_id

def __manage_currency(models, currency_data, resolved_dependencies_data):
    currency_id = None
    if currency_data is None:
        code = u"SEK"
        currency_data = {}
    else:
        code = currency_data["code"]
    has_currency = models.Currency.existsBy("code", code)
    if has_currency is False:
        pass_currency_data = {
            "code" : code,
            "symbol" : "??",
            "country" : "??"
        }
        if code == "SEK":
            pass_currency_data["symbol"] = "kr"
            pass_currency_data["country"] = "SE"
        pass_currency_data.update(currency_data)
        currency_id = models.Currency.create(pass_currency_data)
    if currency_id is None:
        currency_id = models.Currency.getValue('id', 'code', code)
    return currency_id

def __manage_transaction(models, transaction_data, resolved_dependencies_data):
    if transaction_data is None:
        raise Exception("Missing transaction data")
    transaction_data.update({
        'group' : 1,
        'account_id' : resolved_dependencies_data["Account"],
        'transaction_category_id' : resolved_dependencies_data["TransactionCategory"],
        'transaction_type_id' : resolved_dependencies_data["TransactionType"],
        'currency_id' : resolved_dependencies_data["Currency"],
    })
    if 'transaction_date' in transaction_data:
        if not common.is_string(transaction_data['transaction_date']):
            transaction_data.update({
                'transaction_date' : common.format_time_struct(transaction_data['transaction_date'])
            })
    if 'accounting_date' in transaction_data:
        if not common.is_string(transaction_data['accounting_date']):
            transaction_data.update({
                'accounting_date' : common.format_time_struct(transaction_data['accounting_date'])
            })
    if 'reference' not in transaction_data:
        transaction_data['reference'] = ''
    transaction_id = models.Transaction.create(transaction_data)
    return transaction_id

def __manage_transaction_category(models, transaction_category_data, resolved_dependencies_data):
    transaction_category_id = None
    if transaction_category_data is None:
        name = u"Övrigt"
    else:
        name = transaction_category_data["name"]
    has_transaction_category = models.TransactionCategory.existsBy("name", name)
    if has_transaction_category is False:
        transaction_category_id = models.TransactionCategory.create({
            "name": name
        })
    if transaction_category_id is None:
        transaction_category_id = models.TransactionCategory.getValue('id', 'name', name)
    return transaction_category_id

def __manage_organization(models, organization_data, resolved_dependencies_data):
    organization_id = None
    if organization_data is None:
        name = u"Okänd"
    else:
        name = account_category_data["name"]
    has_organization = models.Organization.existsBy("name", name)
    if has_organization is False:
        organization_id = models.Organization.create({
            "name" : name
        })
    if organization_id is None:
        organization_id = models.Organization.getValue('id', 'name', name)
    return organization_id

def __manage_account_category(models, account_category_data, resolved_dependencies_data):
    account_category_id = None
    if account_category_data is None:
        name = u"Lönekonto"
    else:
        name = account_category_data["name"]
    has_account_category = models.AccountCategory.existsBy("name", name)
    if has_account_category is False:
        account_category_id = models.AccountCategory.create({
            "name" : name
        })
    if account_category_id is None:
        account_category_id = models.AccountCategory.getValue('id', 'name', name)
    return account_category_id

def __manage_provider(models, provider_data, resolved_dependencies_data):
    provider_id = None
    if provider_data is None:
        name = u"Collector"
    else:
        name = provider_data["name"]
    has_provider = models.Provider.existsBy("name", name)
    if has_provider is False:
        provider_id = models.Provider.create({
            "name" : name
        })
    if provider_id is None:
        provider_id = models.Provider.getValue('id', 'name', name)
    return provider_id

def __manage_security_rate(models, security_rate_data, resolved_dependencies_data):
    """
    TODO: Implement
    """

def __manage_security(models, security_data, resolved_dependencies_data):
    """
    TODO: Implement
    """