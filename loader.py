#!/usr/bin/env python
# -*- coding: utf-8 -*-
import importlib
import os, os.path
from utilities import common
from core.factories.account_formatter_factory import AccountFormatterFactory
from core.factories.account_parser_factory import AccountParserFactory
from core.formatters.account_formatter import AccountFormatter
from core.formatters.swedbank_formatter import SwedbankFormatter
from core.formatters.avanza_formatter import AvanzaFormatter
from core.parsers.regex_parser import RegexParser
from core.parsers.swedbank_parser import SwedbankParser
from core.parsers.avanza_parser import AvanzaParser
from core.config import readConfig

def __load_module(name, folder):
    safe_module_name = common.path_leaf(name)
    if not safe_module_name.startswith("core.%s" % folder):
        safe_module_name.replace(".", "")
        safe_module_name = "%s.%s" % (folder, safe_module_name)
    safe_module = importlib.import_module("%s" % safe_module_name)
    return safe_module

def load_app(app_name, sources, parser_name = None, formatter_name = None, persist = False):
    _core = load_core()
    _sources = load_sources(sources)
    app = {
        'module' : __load_module(app_name, "apps"),
        'parser' : load_parser(parser_name, _core['factories']['parsers']['account_parser_factory']),
        'formatter' : load_formatter(formatter_name, _core['factories']['formatters']['account_formatter_factory']),
        'sources' : _sources,
        'persist' : persist
    }
    app['core'] = _core
    return app

def load_core():
    account_formatter_factories = load_factory({
        'swedbank' : SwedbankFormatter,
        'avanza' : AvanzaFormatter
    }, AccountFormatterFactory)

    account_parser_factories = load_factory({
        'swedbank' : SwedbankParser,
        'avanza' : AvanzaParser
    }, AccountParserFactory)

    core = {
        'factories' : {
            'formatters' : {
                'account_formatter_factory' : account_formatter_factories
            },
            'parsers' : {
                'account_parser_factory' : account_parser_factories
            }
        }
    }
    return core

def load_factory(names, factory):
    _factory = factory()
    for name, factory_type in names.iteritems():
        _factory.set(name, factory_type)
    return _factory

def load_formatter(name, factory):
    return factory.create(name)

def load_parser(name, factory):
    return factory.create(name)

def load_sources(source_name):
    if source_name.endswith(".ini"):
        source_name = source_name.replace(".ini", "")
        source = common.as_obj(readConfig(source_name, "Source"))
        if hasattr(source, 'exact_match'):
            return [source.exact_match]
        else:
            candidate_files = [f for f in os.listdir(source.dir) if os.path.isfile(os.path.join(source.dir, f))]
            if hasattr(source, 'suffix'):
                candidate_files = [x for x in candidate_files if x.endswith(source.suffix)]
            if hasattr(source, 'prefix'):
                candidate_files = [x for x in candidate_files if x.startswith(source.prefix)]
            if hasattr(source, 'filename_like'):
                candidate_files = [x for x in candidate_files if source.filename_like in x]
            files = [os.path.join(source.dir, x) for x in candidate_files]
            return files
    else:
        return [source_name]

def load_models(model_names):
    models = {}
    model_collection = [common.camelcase_to_underscore(model) for model in model_names]
    for table_name in model_collection:
        module = __load_module(table_name, "core.models")
        model_name = common.underscore_to_camelcase(table_name)
        type_ = getattr(module, model_name)
        models[table_name] = {
            'type' : type_,
            'table_name' : table_name,
            'model_name' : model_name
        }
    return models


