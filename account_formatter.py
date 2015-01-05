#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from collections import deque
class AccountFormatter(object):
    def __init__(self):
        pass

    @classmethod
    def format(self, input):
        output = []
        for i in input:
            formatter_deq = deque(self.formatters)
            items = {}
            for token in i:
                if token == ' ':
                    continue
                formatter = formatter_deq.popleft()
                formatted_token = getattr(self, "format_%s" % formatter)(token)
                items[formatter]= formatted_token
            output.append(items)
        return output

    @classmethod
    def format_currency(self, content):
        ret_content = content
        ret_content = ret_content.strip()
        ret_content = ret_content.replace(",", ".")
        ret_content = ret_content.replace(" ", "")
        return float(ret_content)

    @classmethod
    def format_date(self, date_string, date_format):
        return time.strptime(date_string, date_format)