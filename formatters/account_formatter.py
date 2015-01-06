#!/usr/bin/env python
# -*- coding: utf-8 -*-

import core.formatter
class AccountFormatter(core.formatter.Formatter):
    def __init__(self):
        pass

    @classmethod
    def format_currency(self, content):
        ret_content = content
        ret_content = ret_content.strip()
        ret_content = ret_content.replace(",", ".")
        ret_content = ret_content.replace(" ", "")
        return float(ret_content)