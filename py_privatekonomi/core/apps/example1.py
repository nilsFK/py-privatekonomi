#!/usr/bin/env python
# -*- coding: utf-8 -*-
from py_privatekonomi.utilities import helper, common

def execute(sources, parser, formatter, configs):
    contents = helper.execute(sources, parser, formatter, False)
    for content in contents:
        print(content)
    return contents