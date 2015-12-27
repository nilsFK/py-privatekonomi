#!/usr/bin/env python
# -*- coding: utf-8 -*-
class BaseError(Exception):
    def __init__(self, message):
        super(BaseError, self).__init__(message)
        self.message = message

class ParserError(BaseError):
    def __init__(self, message, capture_data = {}):
        super(ParserError, self).__init__(message)
        self.capture_data = capture_data
    def __str__(self):
        return self.message + " " + str(self.capture_data['content'])
        # return self.message + " " + self.capture_data['content']

class FormatterError(BaseError):
    def __init__(self, message, capture_data = {}):
        super(FormatterError, self).__init__(message)
        self.capture_data = capture_data
    def __str__(self):
        if 'token' in self.capture_data:
            return "Unable to correctly format input for token=%(token)s and subformatter=%(subformatter)s: %(input)s)" % {
                'input' : repr(self.message),
                'token' : repr(self.capture_data['token']),
                'subformatter' : repr(self.capture_data['subformatter'])
            }
        elif 'inconsistent_length' in self.capture_data:
            return "Subformatters did not match the produced tokens. tokens length=%(tokens_length)s, subformatters length=%(subformatters_length)s, tokens=%(tokens)s, subformatters=%(subformatters)s" % {
                'tokens_length' : len(self.capture_data['tokens']),
                'subformatters_length' : len(self.capture_data['subformatters']),
                'tokens' : self.capture_data['tokens'],
                'subformatters' : self.capture_data['subformatters']
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

class MissingAppFunctionError(BaseError):
    def __init__(self, message="", capture_data = {}):
        message = "App is missing function: %(fun_name)s (%(app)s)" % {
            'fun_name' : repr(capture_data['fun_name']),
            'app' : repr(capture_data['app'])
        }
        super(MissingAppFunctionError, self).__init__(message)
        self.capture_data = capture_data
        self.message=message
    def __str__(self):
        return self.message

class InvalidContentError(BaseError):
    def __init__(self, message="", capture_data = {}):
        message = "Attempting to parse invalid content %(content)s given source %(source)s" % {
            'content' : repr(capture_data['content']),
            'source' : repr(capture_data['source'])
        }
        super(InvalidContentError, self).__init__(message)
        self.capture_data = capture_data
        self.message = message
    def __str__(self):
        return self.message
