#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.persist import Persist
from utilities import common

class AccountPersist(Persist):
    def __init__(self, models):
        super(AccountPersist, self).__init__(models)
        self._transactions = []
        self._limit = 100

    def _before_process(self):
        self._transaction_group_id = self._models.lookup("TransactionGroup").allocate()

    def _after_process(self):
        self._limit = 0

    def _set_model_data(self, model_data, dep_data, data_id_key, inserted_table_key, comparison_key = "name"):
        if "id" in dep_data:
            model_data[data_id_key] = dep_data["id"]
        else:
            if len(self._inserted[inserted_table_key]) == 1:
                model_data[data_id_key] = self._inserted[inserted_table_key][0]["id"]
            else:
                for ins in self._inserted[inserted_table_key]:
                    if common.unicode(common.decode(ins[comparison_key])) == common.unicode(dep_data[comparison_key]):
                        model_data[data_id_key] = ins["id"]
                        break

    def _persist_transaction(self):
        if len(self._transactions) >= self._limit and len(self._transactions) > 0:
            self._models.lookup("Transaction").createMany(self._transactions)
            self._transactions = []

    def _resolve_transaction(self, transaction_data, dependency_data):
        self._log("Resolving transaction using:", dependency_data, "and", transaction_data)
        self._log("inserted at transaction point: " + repr(self._inserted))
        for dep_model, dep_data in dependency_data.iteritems():
            if dep_data is None:
                raise Exception(dep_model + " is missing from formatted data, please data gap fill using Persist.fillDataGap")
            if dep_model == 'Account':
                self._set_model_data(transaction_data, dep_data, "account_id", "account")
            elif dep_model == 'TransactionCategory':
                transaction_data["transaction_category_id"] = dep_data["id"]
            elif dep_model == 'Currency':
                self._set_model_data(transaction_data, dep_data, "currency_id", "currency", "code")
            elif dep_model == 'Provider':
                transaction_data["transaction_type_id"] = dep_data["id"]
            elif dep_model == "TransactionType":
                self._set_model_data(transaction_data, dep_data, "transaction_type_id", "transaction_type")

        if 'accounting_date' in transaction_data:
            transaction_data["accounting_date"] = common.format_time_struct(transaction_data["accounting_date"])
        transaction_data["transaction_date"] = common.format_time_struct(transaction_data["transaction_date"])
        transaction_data["group"] = self._transaction_group_id
        self._log("Persist transaction data: " + repr(transaction_data))
        self._transactions.append(transaction_data)
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
            return account_data
        else:
            return None

    def _resolve_currency(self, currency_data, dependency_data):
        self._log("checking for currency_data: " + repr(currency_data))
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

    def _resolve_transaction_group(self, transaction_group_data, dependency_data):
        pass