#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    A sample app which customizes tables
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
from py_privatekonomi.tests.dataset.swedbank.sample1 import test_data as test_data_1

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

class SpecApp(App):
    def execute(self, sources, parser, formatter, configs):
        print("Calling SpecApp.execute")
        contents = helper.execute(
            sources=sources,
            parser=parser,
            formatter=formatter,
            format_as_mapper=False,
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
        models = rebuild_tables(raw_models, customizations)
        return "return something from persist"

def app_1():
    """ An app which persists data """
    print("="*80)
    print("Running app")
    print("="*80)
    db_config = readConfig("db_test", "Database")
    app = AppProxy('spec_app', SpecApp())
    app.setFormatter("swedbank")
    app.setParser("swedbank")
    app.addSources(["samples/swedbank/sample1", "samples/swedbank/sample2"])
    app.persistWith(db_config)
    conf = get_default_config()
    conf['use_logging'] = True
    app.config(conf)
    app.build()
    # print(repr(app))
    app_output = app.run()
    # print(app_output)

if __name__ == '__main__':
    apps = [app_1]
    for app in apps:
        app()
