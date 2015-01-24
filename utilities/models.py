#!/usr/bin/env python
# -*- coding: utf-8 -*-
import loader
from utilities import resolver
import common
from core.model_context import ModelContext

def get_model_name(table_name):
    return common.underscore_to_camelcase(table_name)

def get_table_name(model_name):
    return common.camelcase_to_underscore(model_name)

def get_model_type_mappings(models):
    model_type_mappings = dict((k, v["type"]) for k,v in models.iteritems())
    return model_type_mappings

def get_model_dependencies(model_names):
    models = loader.load_models(model_names)
    model_type_mappings = get_model_type_mappings(models)
    model_types = model_type_mappings.values()
    model_deps = resolver.getModelDependencies(model_types)
    return model_deps

def destroy_tables(model_names):
    context = ModelContext()
    models = loader.load_models(model_names)
    model_deps = get_model_dependencies(model_names)
    model_type_mappings = get_model_type_mappings(models)

    obliteration_order = resolver.resolveObliteration(model_deps)
    for obliterate in obliteration_order:
        model = model_type_mappings[obliterate]
        model(context).obliterate()

def create_tables(model_names):
    context = ModelContext()
    models = loader.load_models(model_names)
    model_deps = get_model_dependencies(model_names)
    generation_order = resolver.resolveGeneration(model_deps)
    model_type_mappings = get_model_type_mappings(models)
    ret_models = {}
    for generate in generation_order:
        model = model_type_mappings[generate]
        ret_models[generate] = model(context).generate()
    return ret_models

def rebuild_tables(model_names):
    destroy_tables(model_names)
    models = create_tables(model_names)
    return models
