#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.persist import Persist
from utilities import common
# import utilities.models as models_utility
"""
    A base class for resolving models into database
    Uses buffer to optimize bulk inserts
"""

class AccountPersist(Persist):
    def __init__(self, models):
        super(AccountPersist, self).__init__(models)

    def _resolve_transaction(self, transaction_data, dependency_data):
        print("Resolving transaction using:", dependency_data, "and", transaction_data)
        if len(self._inserted_ids['account']) > 0:
            transaction_data["account_id"] = list(self._inserted_ids["account"])[0]
        else:
            transaction_data["account_id"] = dependency_data["Account"]["id"]

        if len(self._inserted_ids['transaction_category']) > 0:
            transaction_data["transaction_category_id"] = list(self._inserted_ids["transaction_category"])[0]
        else:
            transaction_data["transaction_category_id"] = dependency_data["TransactionCategory"]["id"]

        if len(self._inserted_ids['transaction_type']) > 0:
            transaction_data["transaction_type_id"] = list(self._inserted_ids["transaction_type"])[0]
        else:
            transaction_data["transaction_type_id"] = dependency_data["TransactionType"]["id"]

        if len(self._inserted_ids['organization']) > 0:
            transaction_data['organization_id'] = list(self._inserted_ids["organization"])[0]
        else:
            transaction_data["organization_id"] = dependency_data["Organization"]["id"]

        if len(self._inserted_ids['provider']) > 0:
            transaction_data['provider_id'] = list(self._inserted_ids["provider"])[0]
        else:
            transaction_data["provider_id"] = dependency_data["Provider"]["id"]

        if len(self._inserted_ids["currency"]) > 0:
            transaction_data["currency_id"] = list(self._inserted_ids["currency"])[0]
        else:
            transaction_data["currency_id"] = dependency_data["Currency"]["id"]
        if 'accounting_date' in transaction_data:
            transaction_data["accounting_date"] = common.format_time_struct(transaction_data["accounting_date"])
        transaction_data["transaction_date"] = common.format_time_struct(transaction_data["transaction_date"])
        print("Constructed transaction data:", transaction_data)
        return transaction_data

    def _resolve_transaction_category(self, transaction_category_data, dependency_data):
        if transaction_category_data is None and self._hasFiller(self._models.lookup("TransactionCategory")):
            return self._filler_data['transaction_category']
        elif transaction_category_data:
            return transaction_category_data
        else:
            return None

    def _resolve_transaction_type(self, transaction_type_data, dependency_data):
        if transaction_type_data is None and self._hasFiller(self._models.lookup("TransactionType")):
            return self._filler_data['transaction_type']
        elif transaction_type_data:
            return transaction_type_data
        else:
            return None

    def _resolve_organization(self, organization_data, dependency_data):
        if organization_data is None and self._hasFiller(self._models.lookup("Organization")):
            return self._filler_data['organization']
        elif organization_data:
            return organization_data
        else:
            return None

    def _resolve_provider(self, provider_data, dependency_data):
        if provider_data is None and self._hasFiller(self._models.lookup("Provider")):
            return self._filler_data['provider']
        elif provider_data:
            return provider_data
        else:
            return None

    def _resolve_account_category(self, account_category_data, dependency_data):
        if account_category_data is None and self._hasFiller(self._models.lookup("AccountCategory")):
            return self._filler_data['account_category']
        elif account_category_data:
            return account_category_data
        else:
            return None

    def _resolve_account(self, account_data, dependency_data):
        if account_data is None and self._hasFiller(self._models.lookup("Account")):
            return self._filler_data['account']
        elif account_data:
            account_data['account_category_id'] = dependency_data['AccountCategory']["id"]
            account_data['organization_id'] = dependency_data['Organization']["id"]
            account_data['provider_id'] = dependency_data['Provider']["id"]
            # print(repr(account_data))
            return account_data
        else:
            return None

    def _resolve_currency(self, currency_data, dependency_data):
        if currency_data is None and self._hasFiller(self._models.lookup("Currency")):
            return self._filler_data['currency']
        elif currency_data:
            return currency_data
        else:
            return None

    def _resolve_security_rate(self, security_rate_data, dependency_data):
        pass

    def _resolve_security(self, security_data, dependency_data):
        pass