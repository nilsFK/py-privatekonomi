#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import parsers.ws_parser as ws_parser
import formatters.swedbank_formatter as swedbank_formatter

argparser = argparse.ArgumentParser(description='Process source (for example, a file) that will be parsed for content into a data structure')
argparser.add_argument('source', metavar='N', type=str, help='Source from which we will parse the general content')
args = argparser.parse_args()

with open(args.source, 'r') as f:
    content = f.readlines()

parser = ws_parser.WhitespaceParser()
parsed = parser.parse(content, r'\t+')

formatter = swedbank_formatter.SwedbankFormatter()
formatted = formatter.format(parsed)
print formatted

