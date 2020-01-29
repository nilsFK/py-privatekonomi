#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from py_privatekonomi.utilities import helper, common

""" Similar to default, but it passes True to sources_as_content  """

def execute(sources, parser, formatter, configs):
    contents = helper.execute(sources=sources,
        parser=parser,
        formatter=formatter,
        format_as_mapper=False,
        sources_is_content=True)
    return contents
