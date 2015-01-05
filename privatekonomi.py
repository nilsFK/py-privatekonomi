#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import parsers.ws_parser as ws_parser
import formatters.swedbank_formatter as swedbank_formatter
import factories.account_formatter_factory
import factories.account_parser_factory

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

argparser = argparse.ArgumentParser(description='Process source (for example, a file) that will be parsed for content into a data structure',
    epilog='Note: if no parser or formatter are given to the command line, the program will attempt to auto-discover the correct formatter/parser for the source, but should not be relied on.')
argparser.add_argument('source',
    metavar='N',
    type=str,
    help='Source from which we will parse and format the general content')
argparser.add_argument('-p', '--parser',
    type=str,
    help='Parser from which we will parse the source')
argparser.add_argument('-f', '--formatter',
    type=str,
    help='Formatter from which we will format the parsed source')
args = argparser.parse_args()

content = read_content(args.source)

parser = get_parser(args.parser)
parsed = parse_content(parser, content)

formatter = get_formatter(args.formatter)
formatted = format_content(formatter, parsed)
print formatted