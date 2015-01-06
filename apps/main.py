#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from models.account import Account
from models.transaction import Transaction
from models.currency import Currency
import core.db
from utilities import helper

def execute(source, parser, formatter):
    content = helper.read_file(source)

    parser = helper.get_parser(parser)
    parsed = parser.parse(content, r'\t+')

    formatter = helper.get_formatter(formatter)
    return formatter.format(parsed)

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