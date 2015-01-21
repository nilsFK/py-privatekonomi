#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import deque
import time
from core.error import FormatterError

class Formatter(object):
    def __init__(self):
        self.__mappings = []
        self.__push_mappings = {}

    def addMapping(self, model_key, subformatter_key, subformatter_value):
        if model_key not in self.__push_mappings:
            self.__push_mappings[model_key] = {}
        self.__push_mappings[model_key][subformatter_key] = subformatter_value

    def format(self, rows, subformatters, format_as_mapper = False):
        self.subformatters = subformatters
        rows  = self.__before_format(rows)
        output = self.__process_rows(rows)
        output = self.__after_format(output)
        return output if not format_as_mapper else self.__mappings

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
        subformatter_deq = deque(self.subformatters)
        for token in row:
            token = token.strip()
            token = self.__callback("before_process_token", token)
            subformatter = subformatter_deq.popleft()
            try:
                formatted_token = getattr(self, "format_%s" % subformatter)(token, subformatter)
            except Exception as e:
                raise FormatterError(e, {
                    'token' : token,
                    'subformatter' : subformatter
                })
            tokens[subformatter] = formatted_token
            self.__callback("after_process_token", formatted_token)
        self.__mappings.append(self.__push_mappings)
        self.__push_mappings = {}
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