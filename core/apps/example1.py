#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utilities import helper, common

""" This is the simplest form of an app possible.
    It defines only an execute function that will
    print the contents of the execution and not much
    more """

def execute(sources, parser, formatter):
    contents = helper.execute(sources, parser, formatter, False)
    for content in contents:
        print content
    return contents