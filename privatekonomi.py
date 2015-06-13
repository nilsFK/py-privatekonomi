#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import loader
from py_privatekonomi.utilities import helper
from py_privatekonomi.utilities.common import as_obj
from py_privatekonomi.core import config

def get_default_config():
    return {
        # Log output from persisting?
        "use_logging" : False,
        # Log to file? Set to full path name to enable, otherwise set to False
        "log_to_file" : False,
        # How many rows to batch insert at a time (might affect performance)
        "insert_rows" : 100,
        # database settings
        "database" : {}
    }

if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='Process source (for example, a file) that will be parsed for content into a data structure')
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
    argparser.add_argument('-a', '--app',
        type=str,
        help='The app which will accept the parsed and formatted content',
        required=True)
    argparser.add_argument('-pe', '--persist',
        action='store_true',
        default=False,
        help='Persists results of parsing/formatting to database. Requires a valid dialect.')
    args = argparser.parse_args()

    app = loader.load_app(args.app, args.source, args.parser, args.formatter, args.persist)

    config_content = as_obj(get_default_config())
    db_config = config.readConfig("db", "Database")
    config_content.database = as_obj(db_config)
    result = helper.execute_app(app, config_content)
