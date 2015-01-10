#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import deque
import time
class Formatter(object):
    def __init__(self):
        pass
        # self._formatters = None

    @classmethod
    def format(self, rows):
        rows  = self.__before_format(rows)
        output = self.__process_rows(rows)
        output = self.__after_format(output)
        return output

    @classmethod
    def __process_rows(self, rows):
        output = []
        items = {}
        for row in rows:
            row = self.__callback("before_process_line", row)
            items = {}
            tokens = self.__process_row(row)
            print tokens
            items.update(tokens)
            self.__callback("after_process_line")
            output.append(items)
        return output

    @classmethod
    def __process_row(self, row):
        print self.formatters
        tokens = {}
        formatter_deq = deque(self.formatters)
        for token in row:
            token = token.strip()
            token = self.__callback("before_process_token", token)
            formatted_token = token
            if len(token) > 0:
                formatter = formatter_deq.popleft()
                formatted_token = getattr(self, "format_%s" % formatter)(token)
                tokens[formatter] = formatted_token
            self.__callback("after_process_token", formatted_token)
        return tokens

    @classmethod
    def __before_format(self, lines):
        lines = self.__callback("before_format", lines)
        return lines

    @classmethod
    def __after_format(self, output):
        output = self.__callback("after_format", output)
        return output

    @classmethod
    def __callback(self, name, args = []):
        attr = getattr(self, name, None)
        if callable(attr):
            return attr(args)
        return args

    @classmethod
    def _format_date(self, date_string, date_format):
        return time.strptime(date_string, date_format)
