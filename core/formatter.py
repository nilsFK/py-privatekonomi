#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import deque
import time
class Formatter(object):
    def __init__(self):
        pass

    def format(self, rows, subformatters):
        self.subformatters = subformatters
        rows  = self.__before_format(rows)
        output = self.__process_rows(rows)
        output = self.__after_format(output)
        return output

    def __process_rows(self, rows):
        output = []
        items = {}
        for row in rows:
            row = self.__callback("before_process_line", row)
            items = {}
            tokens = self.__process_row(row)
            items.update(tokens)
            self.__callback("after_process_line")
            output.append(items)
        return output

    def __process_row(self, row):
        tokens = {}
        formatter_deq = deque(self.subformatters)
        for token in row:
            token = token.strip()
            token = self.__callback("before_process_token", token)
            formatter = formatter_deq.popleft()
            formatted_token = getattr(self, "format_%s" % formatter)(token)
            tokens[formatter] = formatted_token
            self.__callback("after_process_token", formatted_token)
        return tokens


    def __before_format(self, lines):
        lines = self.__callback("before_format", lines)
        return lines

    def __after_format(self, output):
        output = self.__callback("after_format", output)
        return output

    def __callback(self, name, args = []):
        attr = getattr(self, name, None)
        if callable(attr):
            return attr(args)
        return args

    @classmethod
    def _format_date(self, date_string, date_format):
        return time.strptime(date_string, date_format)
