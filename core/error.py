#!/usr/bin/env python
# -*- coding: utf-8 -*-
class BaseError(Exception):
    def __init__(self, message):
        super(BaseError, self).__init__(message)

class ParserError(BaseError):
    def __init__(self, message, errors = {}):
        super(ParserError, self).__init__(message)
    def __str__(self):
        return repr(self.message)

class FormatterError(BaseError):
    def __init__(self, message, errors = {}):
        super(FormatterError, self).__init__(message)
        self.errors = errors
    def __str__(self):
        return "Unable to correctly format input for token=%(token)s and subformatter=%(subformatter)s: %(input)s)" % {
            'input' : repr(self.message),
            'token' : repr(self.errors['token']),
            'subformatter' : repr(self.errors['subformatter'])
        }

class MapperError(BaseError):
    def __init__(self, message="", errors = {}):
        message = "Invalid mapped model name: %(model_name)s of subformatter=%(subformatter)s (use any of %(valid_model_names)s)" % {
            'model_name' : repr(errors['model_name']),
            'subformatter' : repr(errors['subformatter']),
            'valid_model_names' : repr(sorted(errors['valid_model_names']))
        }
        super(MapperError, self).__init__(message)
        self.errors = errors
    def __str__(self):
        pass