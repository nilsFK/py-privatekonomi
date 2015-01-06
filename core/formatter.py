#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque
import time
class Formatter(object):
    def __init__(self):
        pass

    @classmethod
    def format(self, input):
        output = []
        for i in input:
            formatter_deq = deque(self.formatters)
            items = {}
            for token in i:
                token = token.strip()
                if len(token) == 0:
                    continue
                formatter = formatter_deq.popleft()
                formatted_token = getattr(self, "format_%s" % formatter)(token)
                items[formatter]= formatted_token
            output.append(items)
        return output

    @classmethod
    def format_date(self, date_string, date_format):
        return time.strptime(date_string, date_format)