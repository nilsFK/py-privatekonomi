#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import loader
from utilities import helper
from utilities.common import as_obj
from core import config

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

    config = as_obj(get_default_config())
    db_config = config.readConfig("db", "Database")
    config.database = as_obj(db_config)
    result = helper.execute_app(app, config)

class App:
    def __init__(self):
        self.__formatter = None
        self.__parser = None
        self.__source = None
        self.__persist = False
        self.__config =  {}
        self.__db = {}
        self.app = None

    def setFormatter(self, formatter_name):
        self.__formatter = formatter_name

    def setParser(self, parser_name):
        self.__parser = parser_name

    def setSource(self, source_name):
        self.__source = source_name

    def persistWith(self, database_settings):
        self.__persist = True
        self.__db = database_settings

    def config(self, conf):
        self.__config.update(conf)

    def build(self):
        if self.__formatter is None:
            raise Exception("Formatter has not been specified")
        if self.__parser is None:
            raise Exception("Parser has not been specified")
        if self.__source is None:
            raise Exception("Source has not been specified")

        if len(self.__db) > 0:
            self.__config['database'] = self.__db

        internal_app = "core.apps.default"
        if self.__persist is True:
            internal_app = "core.apps.example4"
        self.app = loader.load_app(internal_app, self.__source, self.__parser, self.__formatter, self.__persist)
        return self

    def run(self):
        return helper.execute_app(self.app, as_obj(self.__config))

    def __repr__(self):
        return "App %s" % (repr(self.__config))
