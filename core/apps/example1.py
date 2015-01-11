#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utilities import helper, common

def execute(source, parser, formatter):
    content =  helper.execute(source, parser, formatter)
    print content
    return content