#!/usr/bin/env python
# -*- coding: utf-8 -*-
import importlib
from utilities import common
from core.factories.account_formatter_factory import AccountFormatterFactory
from core.factories.account_parser_factory import AccountParserFactory
from core.formatters.account_formatter import AccountFormatter
from core.formatters.swedbank_formatter import SwedbankFormatter
from core.parsers.regex_parser import RegexParser
from core.parsers.swedbank_parser import SwedbankParser

def __load_module(name, folder):
    safe_module_name = common.path_leaf(name)
    if not safe_module_name.startswith("core.%s" % folder):
        safe_module_name.replace(".", "")
        safe_module_name = "%s.%s" % (folder, safe_module_name)
    safe_module = importlib.import_module("%s" % safe_module_name)
    return safe_module

def load_app(app_name, source, parser_name, formatter_name, persist = False):
    _core = load_core()
    app = {
        'module' : __load_module(app_name, "apps"),
        'parser' : load_parser(parser_name, _core['factories']['parsers']['account_parser_factory']),
        'formatter' : load_formatter(formatter_name, _core['factories']['formatters']['account_formatter_factory']),
        'source' : source,
        'persist' : persist
    }
    app['core'] = _core
    return app

def load_core():
    core = {
        'factories' : {
            'formatters' : {
                'account_formatter_factory' : load_factory('swedbank', AccountFormatterFactory, SwedbankFormatter)
            },
            'parsers' : {
                'account_parser_factory' : load_factory('swedbank', AccountParserFactory, SwedbankParser)
            }
        }
    }
    return core

def load_factory(name, factory, factory_type):
    factory = factory()
    factory.set(name, factory_type)
    return factory

def load_formatter(name, factory):
    return factory.create(name)

def load_parser(name, factory):
    return factory.create(name)