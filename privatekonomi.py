#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import factories.account_formatter_factory
import factories.account_parser_factory
from models.account import Account
from models.transaction import Transaction
from models.currency import Currency
import lib.db

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

def execute(source, parser = None, formatter = None):
    content = read_content(source)

    parser = get_parser(parser)
    parsed = parse_content(parser, content)

    formatter = get_formatter(formatter)
    return format_content(formatter, parsed)

def persist(output):
    lib.db.DB().connect()
    Account().generate()
    Transaction().generate()
    Currency().generate()

if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='Process source (for example, a file) that will be parsed for content into a data structure',
        epilog='Note: if no parser or formatter are given to the command line, the program will attempt to auto-discover the correct formatter/parser for the source, but should not be relied on.')
    argparser.add_argument('source',
        metavar='N',
        type=str,
        help='Source from which we will parse and format the general content')
    argparser.add_argument('-p', '--parser',
        type=str,
        help='Parser from which we will parse the source',
        required=True)
    argparser.add_argument('-f', '--formatter',
        type=str,
        help='Formatter from which we will format the parsed source',
        required=True)
    argparser.add_argument('-pe', '--persist',
        type=bool,
        help='Persist results of parsing/formatting to database. Requires a valid dialect.')
    args = argparser.parse_args()

    output = execute(args.source, args.parser, args.formatter)
    print(output)
    if args.persist:
        persist(output)