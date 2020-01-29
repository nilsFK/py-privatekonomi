#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
import py_privatekonomi.core.parser
import re

class RegexParser(py_privatekonomi.core.parser.Parser):
    def __init__(self):
        pass

    def parse(self, content, re_splitter = None):
        parsed = []
        for c in content:
            c = c.strip()
            if re_splitter is None:
                parsed.append(c.split())
            else:
                parsed.append(re.split(re_splitter, c))
        return parsed