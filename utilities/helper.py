#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.factories.account_formatter_factory import AccountFormatterFactory
from core.factories.account_parser_factory import AccountParserFactory
import core.db
from core.error import MissingAppFunctionError
from utilities import common
import sys

def get_parser(acc_type):
    return AccountParserFactory().create(acc_type)

def get_formatter(acc_type):
    return AccountFormatterFactory().create(acc_type)

def execute_app(app):
    if hasattr(app['module'], 'execute'):
        content = app['module'].execute(app['sources'], app['parser'], app['formatter'])
    else:
        raise MissingAppFunctionError(capture_data={
            'fun_name' : 'execute',
            'app' : app
        })
    if app['persist']:
        if hasattr(app['module'], 'persist'):
            core.db.DB().connect()
            app['module'].persist(content)
        else:
            raise MissingAppFunctionError(capture_data={
                'fun_name' : 'persist',
                'app' : app
            })
    return content

def execute(sources, parser, formatter, format_as_mapper = False):
    contents = []
    for source in sources:
        content = common.read_file(source)
        parsed, subformatters = parser.parse(content)
        content = formatter.format(parsed, subformatters, format_as_mapper)
        contents.append(content)
    return contents