#!/usr/bin/env python
# -*- coding: utf-8 -*-
class BaseError(Exception):
    def __init__(self, message):
        super(BaseError, self).__init__(message)

class ParserError(BaseError):
    def __init__(self, message, capture_data = {}):
        super(ParserError, self).__init__(message)
    def __str__(self):
        return repr(self.message)

class FormatterError(BaseError):
    def __init__(self, message, capture_data = {}):
        super(FormatterError, self).__init__(message)
        self.capture_data = capture_data
    def __str__(self):
        return "Unable to correctly format input for token=%(token)s and subformatter=%(subformatter)s: %(input)s)" % {
            'input' : repr(self.message),
            'token' : repr(self.capture_data['token']),
            'subformatter' : repr(self.capture_data['subformatter'])
        }

class MapperError(BaseError):
    def __init__(self, message="", capture_data = {}):
        message = "Invalid mapped model name: %(model_name)s of subformatter=%(subformatter)s (use any of %(valid_model_names)s)" % {
            'model_name' : repr(capture_data['model_name']),
            'subformatter' : repr(capture_data['subformatter']),
            'valid_model_names' : repr(sorted(capture_data['valid_model_names']))
        }
        super(MapperError, self).__init__(message)
        self.capture_data = capture_data
    def __str__(self):
        pass