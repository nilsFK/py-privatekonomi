#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import deque
import time
from py_privatekonomi.core.error import FormatterError
from py_privatekonomi.utilities.common import (
    is_string,
    is_date,
    is_datetime,
    format_date,
    format_datetime
)

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
        rows = self.__before_format(rows)
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
        if len(row) != len(self.subformatters):
            raise FormatterError(Exception, {
                'inconsistent_length' : True,
                'subformatters' : self.subformatters,
                'tokens' : row
            })
        subformatter_deq = deque(self.subformatters)
        for token in row:
            if is_string(token):
                token = token.strip()
            token = self.__callback("before_process_token", token)
            subformatter = subformatter_deq.popleft()
            try:
                if subformatter is not None:
                    formatted_token = getattr(self, "format_%s" % subformatter)(token, subformatter)
                else:
                    formatted_token = token
            except Exception as e:
                raise FormatterError(e, {
                    'token' : token,
                    'subformatter' : subformatter
                })
            if subformatter is not None:
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
        if is_string(date_string):
            if date_format is None:
                if len(date_string) == 10:
                    date_format = '%Y-%m-%d'
                elif len(date_string) == 8:
                    date_format = '%y-%m-%d'
            return time.strptime(date_string, date_format)
        elif is_date(date_string):
            return format_date(date_string)
        elif is_datetime(date_string):
            return format_datetime(date_string)
        else:
            return date_string
