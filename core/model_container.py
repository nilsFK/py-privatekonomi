#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import MetaData
from utilities import common
from utilities.models import get_table_name
from utilities.models import get_model_name

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
        self.__models = common.as_dict(models)

    def lookup(self, lookup_by):
        lookup = get_table_name(lookup_by)
        return self.__models[get_model_name(lookup)]

    def asTableName(self, model):
        if common.is_string(model):
            model_name = model
        else:
            model_name = model.getNormalizedName()
        return get_table_name(model_name)

    def asModelName(self, model):
        pass

    def all(self):
        return common.as_obj(self.__models)

    def internal(self):
        return self.__models

