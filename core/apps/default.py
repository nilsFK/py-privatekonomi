#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utilities import helper, common

def execute(sources, parser, formatter):
    contents = helper.execute(sources, parser, formatter, False)
    return contents

def persist(output):
    return output