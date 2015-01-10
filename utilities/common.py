#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ntpath
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