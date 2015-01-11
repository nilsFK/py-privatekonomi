#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ntpath, time
class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)

def as_obj(to_obj):
    return Struct(**to_obj)

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