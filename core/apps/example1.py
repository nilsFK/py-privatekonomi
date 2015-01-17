#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utilities import helper, common

def execute(sources, parser, formatter):
    contents = helper.execute(sources, parser, formatter)
    for content in contents:
        print content
    return contents