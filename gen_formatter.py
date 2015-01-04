#!/usr/bin/env python
# -*- coding: utf-8 -*-

# requires Python 3.3.x+
class GenFormatter(object):
    def __init__(self):
        pass

    @classmethod
    def format(self):
        pass

    @classmethod
    def format_currency(self, content):
        ret_content = content
        ret_content = ret_content.strip()
        ret_content = ret_content.replace(",", ".")
        ret_content = ret_content.replace(" ", "")
        return float(ret_content)