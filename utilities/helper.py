#!/usr/bin/env python
# -*- coding: utf-8 -*-

from factories.account_formatter_factory import AccountFormatterFactory
from factories.account_parser_factory import AccountParserFactory
from utilities import common

def get_parser(acc_type):
    return AccountParserFactory().createAccountParser(acc_type)

def get_formatter(acc_type, formatters):
    return AccountFormatterFactory().createAccountFormatter(acc_type, formatters)

def execute(source, parser, formatter):
    content = common.read_file(source)

    parser = get_parser(parser)
    parsed, formatters = parser.parse(content)

    formatter = get_formatter(formatter, formatters)
    return formatter.format(parsed)
