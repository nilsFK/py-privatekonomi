#!/usr/bin/env python
# -*- coding: utf-8 -*-

import core.parser
import re

class WhitespaceParser(core.parser.Parser):
    def __init__(self):
        pass

    def parse(self, content, re_splitter = None):
        parsed = []
        for c in content:
            if re_splitter is None:
                parsed.append(c.split())
            else:
                parsed.append(re.split(re_splitter, c))
        return parsed