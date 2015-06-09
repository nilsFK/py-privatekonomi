#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utilities import helper, common

""" This is the simplest form of an app possible.
    It defines only an execute function that executes
    the app and a persist function that simply returns
    the output back again """

def execute(sources, parser, formatter, configs):
    contents = helper.execute(sources, parser, formatter, False)
    return contents
