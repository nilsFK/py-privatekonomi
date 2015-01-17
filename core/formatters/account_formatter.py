#!/usr/bin/env python
# -*- coding: utf-8 -*-
import core.formatter
from core.formatter import Formatter
class AccountFormatter(Formatter):
    def __init__(self):
        super(AccountFormatter, self).__init__()

    @classmethod
    def _format_currency(self, content):
        try:
            ret_content = content
            ret_content = ret_content.strip()
            ret_content = ret_content.replace(",", ".")
            ret_content = ret_content.replace(" ", "")
            val = float(ret_content)
            return val
        except ValueError:
            return None

    @classmethod
    def _format_float(self, content):
        try:
            ret_content = content
            ret_content = ret_content.strip()
            ret_content = ret_content.replace(",", ".")
            ret_content = ret_content.replace(" ", "")
            val = float(ret_content)
            return val
        except ValueError:
            return None

    @classmethod
    def _deformat_currency(self, content):
        ret_content = str(content)
        ret_content = ret_content.replace(".", ",")
        if ret_content.endswith(",0"):
            ret_content += "0"
        return ret_content

