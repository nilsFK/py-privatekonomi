#!/usr/bin/env python
# -*- coding: utf-8 -*-

from account_parser import AccountParser
import re

class WhitespaceParser(AccountParser):
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