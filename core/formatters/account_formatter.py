#!/usr/bin/env python
# -*- coding: utf-8 -*-
import core.formatter
from core.formatter import Formatter
class AccountFormatter(Formatter):
    def __init__(self):
        super(AccountFormatter, self).__init__()

    @classmethod
    def _format_currency(self, content):
        ret_content = content
        ret_content = ret_content.strip()
        ret_content = ret_content.replace(",", ".")
        ret_content = ret_content.replace(" ", "")
        return float(ret_content)