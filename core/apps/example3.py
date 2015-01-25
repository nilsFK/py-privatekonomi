#!/usr/bin/env python
# -*- coding: utf-8 -*-

import core.db
from core.mappers.account_mapper import AccountMapper
from utilities import helper
from utilities.common import decode
from utilities import resolver
from utilities.models import rebuild_tables, get_dependency_order
from utilities import helper, common
import loader

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
    for data in content:
        for model in dependency_order:
            if model in data:
                print model, ":", data[model]
            else:
                print "Missing model:", model
            print "-"*40
        print "="*80
    print "*"*80