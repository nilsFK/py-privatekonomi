#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.factories.account_formatter_factory import AccountFormatterFactory
from core.factories.account_parser_factory import AccountParserFactory
from utilities import common
import sys
import pprint

def get_parser(acc_type):
    return AccountParserFactory().create(acc_type)

def get_formatter(acc_type):
    return AccountFormatterFactory().create(acc_type)

def execute_app(app):
    content = app['module'].execute(app['sources'], app['parser'], app['formatter'])
    if app['persist']:
        app['module'].persist(content)
    return content

def execute(sources, parser, formatter, format_as_mapper):
    contents = []
    for source in sources:
        content = common.read_file(source)
        parsed, subformatters = parser.parse(content)
        content = formatter.format(parsed, subformatters, format_as_mapper)
        contents.append(content)
    return contents
