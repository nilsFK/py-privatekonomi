#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import MetaData
from utilities import common

"""
A container class for models
Abstracts away some of the details of having to convert between
table names and model names to find a particular model.
Model lookup can be made using:

* table names
* model names
* model types

For example, table name "account_category", model name "AccountCategory", and model type AccountCategory
all refer to the same model, so all of the following return the same model:
    model_container = ModelContainer(models)
    model_container.lookup("account_category")
    model_container.lookup("AccountCategory")
    model_container.lookup(AccountCategory)

Internally keys are stored as table names

"""
class ModelContainer(object):
    def __init__(self, models):
        self.__models = models

    def lookup(lookup_by):
        pass

