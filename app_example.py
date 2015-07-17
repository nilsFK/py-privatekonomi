#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    A sample app which parses and formats Swedbank transactions
    and prints resulting contents
"""
from py_privatekonomi.utilities import helper
from py_privatekonomi.utilities.models import rebuild_tables, create_tables
from py_privatekonomi.core import loader
from py_privatekonomi.core.app import (App, AppProxy)
from py_privatekonomi.core.config import readConfig
from py_privatekonomi.core.mappers.economy_mapper import EconomyMapper
from py_privatekonomi.tests.dataset.swedbank.sample1 import test_data as test_data_1

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

class MyApp(App):
    def execute(self, sources, parser, formatter, configs):
        print("Calling MyApp.execute")
        contents = helper.execute(
            sources=sources,
            parser=parser,
            formatter=formatter,
            format_as_mapper=False,
            sources_is_content=configs.sources_is_content
            )
        return contents

    def persist(self, output, configs):
        print("Calling MyApp.persist")
        models = rebuild_tables(loader.load_models(EconomyMapper.getModelNames()))
        return "return something from persist"

def app_1(num):
    """ An app which formats and parses two Swedbank samples """
    print("="*80)
    print("Running app " + str(num))
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
    app_output = app.run()
    print(app_output)

def app_2(num):
    """ An app which formats and parses two Avanza samples """
    print("="*80)
    print("Running app " + str(num))
    print("="*80)
    app = AppProxy('name_of_my_app', MyApp())
    app.setFormatter("avanza")
    app.setParser("avanza")
    app.addSources(["samples/avanza/sample1"])
    conf = get_default_config()
    conf['use_logging'] = True
    app.config(conf)
    app.build()
    print(repr(app))
    app_output = app.run()
    print(app_output)

def app_3(num):
    """ An app which sets the output directly without going through the process
        of parsing and formatting """
    print("="*80)
    print("Running app " + str(num))
    print("="*80)
    app = AppProxy('name_of_my_app', MyApp())
    conf = get_default_config()
    conf['use_logging'] = True
    app.config(conf)
    app.setOutput([test_data_1])
    app.build()
    print(repr(app))
    app_output = app.run()
    print(app_output)

def app_4(num):
    """ An app which guesses the formatter and parser by calling
        autodiscover() """
    print("="*80)
    print("Running app #" + str(num))
    print("="*80)
    app = AppProxy('name_of_my_app', MyApp())
    app.autodiscover([
        {
            'formatter' : 'avanza',
            'parser' : 'avanza'
        },
        {
            'formatter' : 'some_unknown_formatter',
            'parser' : 'some_unknown_parser'
        },
        {
            'formatter' : 'swedbank',
            'parser' : 'swedbank'
        }
    ])
    conf = get_default_config()
    conf['use_logging'] = True
    app.config(conf)

    print("-"*80)
    print("Swedbank samples")
    print("-"*80)
    app.addSources(["samples/swedbank/sample1","samples/swedbank/sample2"])
    app.build()
    print(repr(app))
    app_output = app.run()
    print(app_output)

    print("-"*80)
    print("Avanza samples")
    print("-"*80)
    app.clearSources()
    app.addSources(["samples/avanza/sample1"])
    app.build()
    app_output = app.run()
    print(app_output)

if __name__ == '__main__':
    apps = [app_1, app_2, app_3, app_4]
    for num, app in enumerate(apps):
        app(num+1)
