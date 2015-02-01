#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utilities import resolver
import common
from core.model_context import ModelContext

"""
    Collects a variety of functions to help with models.

    Terminology:
    ============
    model_name: Name of a model, e.g. Transaction, Account, TransactionCategory, etc.
    model_names: Collection of model_name, usually list
    table_name: Name of a table, e.g. transaction, account, transaction_category, etc.
    table_names: Collection of table_name, usually list
    model_struct: A common.Struct with the key being the name of the model, e.g:
            _models = rebuild_tables(AccountMapper.getModelNames())
            _models.Transaction.insert(...)
        where Transaction is the model struct within the _models object
        can be converted back to dict using common.as_dict(models)
"""

def get_model_name(table_name):
    return common.underscore_to_camelcase(str(table_name))

def get_table_name(model_name):
    return common.camelcase_to_underscore(model_name)

def get_model_type_mappings(models):
    model_type_mappings = {}
    for model, values in models.iteritems():
        if isinstance(values, dict):
            model_type_mappings[model] = values["type"]
        else:
            model_type_mappings[model] = type(values)
    return model_type_mappings

def get_model_dependencies(models):
    model_type_mappings = get_model_type_mappings(models)
    model_types = model_type_mappings.values()
    model_deps = resolver.getModelDependencies(model_types)
    return model_deps

def get_model_dependencies_struct(model_struct):
    model_names = common.as_dict(model_struct)
    model_deps = get_model_dependencies(model_names)
    return model_deps

def get_dependency_order(model_struct):
    model_deps = get_model_dependencies_struct(model_struct)
    generation_order = resolver.resolveGeneration(model_deps)
    generation_order = [get_model_name(generate) for generate in generation_order]
    return generation_order

def destroy_tables(models):
    context = ModelContext()
    model_deps = get_model_dependencies(models)
    model_type_mappings = get_model_type_mappings(models)

    obliteration_order = resolver.resolveObliteration(model_deps)
    for obliterate in obliteration_order:
        model = model_type_mappings[obliterate]
        model(context).obliterate()

def create_tables(models):
    context = ModelContext()
    model_deps = get_model_dependencies(models)
    generation_order = resolver.resolveGeneration(model_deps)
    model_type_mappings = get_model_type_mappings(models)
    ret_models = {}
    for generate in generation_order:
        model = model_type_mappings[generate]
        ret_models[get_model_name(generate)] = model(context).generate()
    return common.as_obj(ret_models)

def rebuild_tables(models):
    destroy_tables(models)
    models = create_tables(models)
    return models
