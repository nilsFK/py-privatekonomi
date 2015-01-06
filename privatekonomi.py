#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import apps.main

def execute(source, parser, formatter):
    return apps.main.execute(source, parser, formatter)

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
        apps.main.persist(output)