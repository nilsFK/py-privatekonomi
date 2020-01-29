#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals
from py_privatekonomi.core.factories.account_formatter_factory import AccountFormatterFactory
from py_privatekonomi.core.factories.account_parser_factory import AccountParserFactory
import py_privatekonomi.core.db
from py_privatekonomi.core.error import (
    MissingAppFunctionError,
    InvalidContentError
)
from py_privatekonomi.core import loader
from py_privatekonomi.utilities import common, excel
import sys, os

def get_parser(acc_type):
    return AccountParserFactory().create(acc_type)

def get_formatter(acc_type):
    return AccountFormatterFactory().create(acc_type)

def get_customizations(org_name, raw_models):
    customizations = loader.load_customizations(org_name, raw_models)
    return customizations

def execute_app(app, config = None):
    if hasattr(app['module'], 'execute'):
        content = app['module'].execute(app['sources'], app['parser'], app['formatter'], config)
    else:
        raise MissingAppFunctionError(capture_data={
            'fun_name' : 'execute',
            'app' : app
        })
    if app['persist']:
        if hasattr(app['module'], 'persist'):
            connect_db(config.database)
            app['module'].persist(content, config)
        else:
            raise MissingAppFunctionError(capture_data={
                'fun_name' : 'persist',
                'app' : app
            })
    return content

def execute(sources, parser, formatter, format_as_mapper = False, sources_is_content=False):
    contents = []
    options = {}
    for source in sources:
        if sources_is_content:
            if not common.is_list(source):
                source = [s.strip() for s in source.splitlines()]
            content = source
        else:
            filetype = identify_filetype(source)
            options['filetype'] = filetype
            if filetype == 'excel':
                content = excel.get_content(source, 0)
            else:
                content = common.read_file(source)
        if content is False or content is None or len(content) == 0:
            raise InvalidContentError(capture_data={
                "content" : content,
                "source": source
            })
        parsed, subformatters = parser.parse(content, options)
        content = formatter.format(parsed, subformatters, format_as_mapper)
        contents.append(content)
    return contents

def connect_db(db_config):
    py_privatekonomi.core.db.DB().connect(db_config)

def identify_filetype(filepath):
    """ supported subset of filetypes, unknown filetype returns None
    not very smart, just checks file name to decide, could be improved
    by peeking at the file """
    known_filetypes = {
        'xls' : 'excel',
        'xlsx' : 'excel',
        'csv' : 'csv',
        '' : 'empty'
    }
    filename, file_ext = os.path.splitext(filepath)
    file_ext = file_ext.replace(".", "")
    if file_ext in known_filetypes:
        return known_filetypes[file_ext]
    else:
        return None