#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
common.py is common low-level functionality
and should not import anything except for
built in packages.
"""
import ntpath
import time, datetime
import codecs
import re
import sys
import decimal

if sys.version < '3':
    import codecs
    def u(x):
        return codecs.unicode_escape_decode(x)[0]
else:
    def u(x):
        return x

class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)
    def __repr__(self):
        return repr(self.__dict__)

def as_obj(to_obj):
    return Struct(**to_obj)

def as_dict(from_obj):
    return from_obj.__dict__

def singleton(cls):
    obj = cls()
    # Always return the same object
    cls.__new__ = staticmethod(lambda cls: obj)
    # Disable __init__
    try:
        del cls.__init__
    except AttributeError:
        pass
    return cls

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def read_file(file_path):
    try:
        with codecs.open(file_path, 'r', 'utf-8') as f:
            content = f.readlines()
    except:
        with open(file_path, 'r') as f:
            content = f.readlines()
    return content

def write_file(file_path, content, create_if_missing=False):
    options = "w+" if create_if_missing else "w"
    with open(file_path, options) as f:
        f.write(content)

def append_file(file_path, content):
    with open(file_path, "a") as f:
        f.write(content)

def format_time_struct(time_struct, format='%Y-%m-%d'):
    return time.strftime(format, time_struct)

def format_date(date, format='%Y-%m-%d'):
    return date.strftime(format)

def is_time_struct(data):
    return isinstance(data, time.struct_time)

def is_date(data):
    return isinstance(data, datetime.date)

def is_datetime(data):
    return isinstance(data, datetime.datetime)

def is_decimal(data):
    return isinstance(data, decimal.Decimal)

def is_unicode(s):
    if sys.version < '3':
        return isinstance(s, unicode)
    else:
        return isinstance(s, str)

def decode(val):
    """Since we in most cases are not aware of
    the true encoding we try to decode it from
    utf-8, if that fails we decode it as latin-1,
    if that fails we return it as is.
    Note that we attempt decoding in this order
    because py-privatekonomi only works with
    utf-8 and latin-1
    """
    try:
        val = val.decode("utf-8")
    except:
        try:
            val = val.decode("latin-1")
        except:
            pass
    return val

if sys.version < '3':
    __unicode = unicode
    def unicode(val):
        try:
            val = __unicode(val)
            return val
        except UnicodeDecodeError:
            # Already unicode
            return val
        raise Exception("Invalid unicode: " + val)
else:
    def unicode(val):
        return val

def camelcase_to_underscore(name):
    """ CamelCase to camel_case """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def underscore_to_camelcase(name):
    return ''.join(x.capitalize() or '_' for x in name.split('_'))

def is_string(string):
    is_string_ = False
    if isinstance(string, str):
        is_string_ = True
    try:
        if isinstance(s, basestring):
            is_string_ = True
    except NameError:
        pass
    return is_string_
