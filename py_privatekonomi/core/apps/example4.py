#!/usr/bin/env python
# -*- coding: utf-8 -*-

import py_privatekonomi.core.db
from py_privatekonomi.core.mappers.economy_mapper import EconomyMapper
from py_privatekonomi.utilities import helper
from py_privatekonomi.utilities.models import rebuild_tables, create_tables
from py_privatekonomi.core import loader
from py_privatekonomi.utilities.common import as_obj
import sys

"""
    An extension of example3.py that does not rebuild tables, but
    create tables from scratch (if necessary).
    If there is any data in the database we fill those data gaps
    that need to be sealed.
"""

def execute(sources, parser, formatter, configs):
    contents = helper.execute(sources, parser, formatter, True) # <--
    return contents

def persist(output, configs):
    models = create_tables(loader.load_models(EconomyMapper.getModelNames()))
    for content in output:
        __persist(content, models, configs)

def __persist(content, models, configs):
    economy_persist = EconomyPersist(models, configs.insert_rows)
    economy_persist.useLogging(configs.use_logging)
    save_output_to_file = configs.log_to_file

    if save_output_to_file is not False:
        orig_stdout = sys.stdout
        f = file(save_output_to_file, "w")
        sys.stdout = f

    # TODO: persist data...

    if save_output_to_file is not False:
        sys.stdout = orig_stdout
        f.close()
