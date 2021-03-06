#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Sample apps that persists data and customizes tables
"""

"""
pype imports
"""
from py_privatekonomi.utilities import helper
from py_privatekonomi.utilities.models import rebuild_tables, create_tables
from py_privatekonomi.core import loader
from py_privatekonomi.core.app import (App, AppProxy)
from py_privatekonomi.core.config import readConfig
from py_privatekonomi.core.mappers.economy_mapper import EconomyMapper
from py_privatekonomi.tests.dataset.nordnet.sample1 import test_data as nordnet_test_data_1
from py_privatekonomi.core.transaction import (TransactionManager, Transaction, CustomTransaction, TransactionHelper)

"""
sqlalchemy imports
"""
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, ForeignKeyConstraint
from sqlalchemy.types import Date, Numeric, DateTime

def get_default_config():
    return {
        # Log output from persisting?
        "use_logging" : False,
        # Log to file? Set to full path name to enable, otherwise set to False
        "log_to_file" : False,
        # How many rows to batch insert at a time (might affect performance)
        "insert_rows" : 100,
        # database settings
        "database" : {},
        # Is sourced passed a list of raw textual transactions rather than
        # a list of files where the raw transactions reside?
        "sources_is_content" : False
    }

class PersistApp(App):
    def createDefaults(self):
        self.account_category_id = self.models.AccountCategory.insert({
            'name' : u'Lönekonto'
        })
        self.organization_id = self.models.Organization.insert({
            'name' : 'Swedbank'
        })
        self.account_id = self.models.Account.insert({
                'name' : u'Mitt Lönekonto',
                'account_code' : '123-123',
                'account_number' : '123456789',
                'current_balance' : 12000.12,
                'future_balance' : 13000.13,
                'account_category_id' : self.account_category_id,
                'organization_id' : self.organization_id,
                'provider_id' : None
        })
        self.transaction_type_id = self.models.TransactionType.insert({
                'name' : u'Default',
        })
        self.transaction_category_id = self.models.TransactionCategory.insert({
                'name' : 'Default'
        })

    def execute(self, sources, parser, formatter, configs):
        print("Calling PersistApp.execute")
        contents = helper.execute(
            sources=sources,
            parser=parser,
            formatter=formatter,
            format_as_mapper=True,
            sources_is_content=configs.sources_is_content
            )
        return contents

    def persist(self, output, configs):
        print("Calling PersistApp.persist")
        self.models = self._rebuildTables()
        self.createDefaults()
        transaction_groups = []
        for content in output:
            self.transaction_manager = TransactionManager(self.models, configs.insert_rows)
            transaction_group = self.__persist(content, configs)
            transaction_groups.append(transaction_group)
        return transaction_groups

    def __persist(self, transactions, configs):
        transaction_group = TransactionHelper.createTransactionGroup(self.models)
        for transaction in transactions:
            t = CustomTransaction(transaction, transaction_group, self.models)
            t.setDefault('account_id', self.account_id)
            t.setDefault('account_category_id', self.account_category_id)
            t.setDefault('organization_id', self.organization_id)
            t.setDefault('transaction_category_id', self.transaction_category_id)

            t.buildTransaction()
            self.transaction_manager.addTransaction(t)
            self.transaction_manager.debuffer()
        self.transaction_manager.forceDebuffer()
        return transaction_group

class SpecApp(App):
    def execute(self, sources, parser, formatter, configs):
        print("Calling SpecApp.execute")
        contents = helper.execute(
            sources=sources,
            parser=parser,
            formatter=formatter,
            format_as_mapper=True,
            sources_is_content=configs.sources_is_content
            )
        return contents

    def persist(self, output, configs):
        print("Calling SpecApp.persist")
        raw_models = loader.load_models(EconomyMapper.getModelNames())

        # This is where the customizations take place:
        # Using customizations we can add columns, remove
        # columns, modify columns
        # To create a customization we must refer to the models
        # lower case underscore form, e.g. Transaction becomes
        # transaction, SecurityRate becomes security_rate, and so on.
        customizations = {}
        customizations[raw_models['transaction']['type']] = {
            # add new custom col
            'custom_col' : Column('custom_col', Integer, nullable=False),
            # modify existing col
            'reference' : Column('reference', String(1024), nullable=False, server_default='empty_ref'),
            # remove existing col, not really recommended
            'created' : None
        }
        customizations[raw_models['account']['type']] = {
            'custom_col' : Column('custom_col', Integer, nullable=True)
        }
        customizations[raw_models['account_category']['type']] = {
            'ac_type' : Column('ac_type', String(128), nullable=True)
        }
        customizations[raw_models['transaction_type']['type']] = {
            'is_public' : Column('is_public', Integer, nullable=False, server_default='0')
        }
        self._rebuildTables(customizations=customizations)
        return "return something from persist"

def app_1():
    """ An app which persists Swedbank data """
    print("="*80)
    print("Running app #1")
    print("="*80)
    db_config = readConfig("db_test", "Database")
    app = AppProxy('spec_app', SpecApp())
    app.setFormatter("swedbank")
    app.setParser("swedbank")
    app.addSources(["samples/swedbank/sample1", "samples/swedbank/sample2", "samples/swedbank/sample5"])
    app.persistWith(db_config)
    conf = get_default_config()
    conf['use_logging'] = True
    app.config(conf)
    app.build()
    app_output = app.run()
    return app_output

def app_2():
    """ An app which persists Avanza data """
    print("="*80)
    print("Running app #2")
    print("="*80)
    db_config = readConfig("db_test", "Database")
    app = AppProxy('persist_app', SpecApp())
    app.setFormatter("avanza")
    app.setParser("avanza")
    app.addSources(["samples/avanza/sample1"])
    app.persistWith(db_config)
    conf = get_default_config()
    conf['use_logging'] = True
    app.config(conf)
    app.build()
    app_output = app.run()
    return app_output

def app_3():
    """ An app which persists Nordnet data """
    print("="*80)
    print("Running app #3")
    print("="*80)
    db_config = readConfig("db_test", "Database")
    app = AppProxy('nordnet_app', PersistApp())
    app.setFormatter("nordnet")
    app.setParser("nordnet")
    app.addSources(["samples/nordnet/sample1.csv"])
    app.persistWith(db_config)
    conf = get_default_config()
    conf['use_logging'] = True
    app.config(conf)
    app.build()
    app_output = app.run()
    return app_output

def app_4():
    """ An app which persists Nordnet data by calling setOutput """
    print("="*80)
    print("Running app #4")
    print("="*80)
    db_config = readConfig("db_test", "Database")
    app = AppProxy('nordnet_output_app', PersistApp())
    app.persistWith(db_config)
    conf = get_default_config()
    conf['use_logging'] = True
    app.config(conf)
    app.setFormatter("nordnet")
    app.setParser("nordnet")
    app.setOutput([nordnet_test_data_1])
    app.build()
    app_output = app.run()
    return app_output

if __name__ == '__main__':
    apps = [
        app_1,
        app_2,
        app_3,
        app_4
    ]
    for num, app in enumerate(apps):
        app_output = app()
        for idx, dataSet in enumerate(app_output['execute']):
            print("Data length (set %s):" % (idx+1), len(dataSet))
            #print(dataSet)

        print("Formatter:", app_output['formatter'])
        print("Parser:", app_output['parser'])
