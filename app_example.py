#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    A sample app which parses and formats Swedbank transactions
    and prints resulting contents
"""
from py_privatekonomi.core.app import (App, AppProxy)
from py_privatekonomi.utilities import helper
from py_privatekonomi.core.persisters.economy_persist import EconomyPersist
from py_privatekonomi.utilities.models import rebuild_tables, create_tables
from py_privatekonomi.core.mappers.economy_mapper import EconomyMapper
from py_privatekonomi.tests.dataset.swedbank.sample1 import test_data as test_data_1
from py_privatekonomi.core.config import readConfig
import loader

def get_default_config():
    return {
        # Log output from persisting?
        "use_logging" : False,
        # Log to file? Set to full path name to enable, otherwise set to False
        "log_to_file" : False,
        # How many rows to batch insert at a time (might affect performance)
        "insert_rows" : 100,
        # database settings
        "database" : {}
    }

class MyApp(App):
    def execute(self, sources, parser, formatter, configs):
        print("Calling execute")
        contents = helper.execute(sources, parser, formatter, False)
        return contents

    def persist(self, output, configs):
        print("Calling persist")

def app_1():
    """ An app which formats and parses two samples """
    print("Running app 1")
    print("="*80)
    app = AppProxy('name_of_my_app', MyApp())
    app.setFormatter("swedbank")
    app.setParser("swedbank")
    app.addSources(["samples/swedbank/sample1", "samples/swedbank/sample2"])
    conf = get_default_config()
    conf['use_logging'] = True
    app.config(conf)
    app.build()
    print(repr(app))
    content = app.run()
    print(content)

def app_2():
    """ An app which sets the output directly without going through the process
        of parsing and formatting """
    print("Running app 2")
    print("="*80)
    app = AppProxy('name_of_my_app', MyApp())
    conf = get_default_config()
    conf['use_logging'] = True
    app.config(conf)
    app.setOutput([test_data_1])
    app.build()
    print(repr(app))
    content = app.run()
    print(content)

if __name__ == '__main__':
    app_1()
    app_2()
