#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import factories.account_formatter_factory
import factories.account_parser_factory
from models.account import Account
from models.transaction import Transaction
from models.currency import Currency
import core.db
def read_content(source):
    with open(source, 'r') as f:
        content = f.readlines()
    return content

def get_parser(acc_type):
    return factories.account_parser_factory.AccountParserFactory().createAccountParser(acc_type)

def parse_content(parser, content):
    return parser.parse(content, r'\t+')

def get_formatter(acc_type):
    return factories.account_formatter_factory.AccountFormatterFactory().createAccountFormatter(acc_type)

def format_content(formatter, content):
    return formatter.format(content)

def execute(source, parser, formatter):
    content = read_content(source)

    parser = get_parser(parser)
    parsed = parse_content(parser, content)

    formatter = get_formatter(formatter)
    return format_content(formatter, parsed)

def persist(output):
    core.db.DB().connect()
    account = Account().obliterate().generate()
    transaction = Transaction().obliterate().generate()
    currency = Currency().obliterate().generate()
    id1 = currency.insertCode("SEK")
    id2 = currency.insertCode("USD")
    code = currency.getCode(id1[0])
    print(id1)
    print(id2)
    print(code)