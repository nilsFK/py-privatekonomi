#!/usr/bin/env python
# -*- coding: utf-8 -*-
import py_privatekonomi.core.formatter
from py_privatekonomi.core.formatter import Formatter
from py_privatekonomi.utilities.common import (
    is_string,
    is_date,
    is_datetime,
    format_date,
    format_datetime
)
class AccountFormatter(Formatter):
    def __init__(self, name):
        super(AccountFormatter, self).__init__()
        self.__name = name

    def getName(self):
        return self.__name

    @classmethod
    def _format_currency(self, content):
        if is_string(content):
            try:
                ret_content = content
                ret_content = ret_content.strip()
                ret_content = ret_content.replace(",", ".")
                ret_content = ret_content.replace(" ", "")
                if ret_content == "-":
                    return None
                else:
                    val = float(ret_content)
                return val
            except ValueError:
                return None
        else:
            return content

    @classmethod
    def _format_float(self, content):
        if is_string(content):
            try:
                ret_content = content
                ret_content = ret_content.strip()
                ret_content = ret_content.replace(",", ".")
                ret_content = ret_content.replace(" ", "")
                val = float(ret_content)
                return val
            except ValueError:
                return None
        else:
            return content

    @classmethod
    def _deformat_currency(self, content):
        ret_content = str(content)
        ret_content = ret_content.replace(".", ",")
        if ret_content.endswith(",0"):
            ret_content += "0"
        return ret_content

