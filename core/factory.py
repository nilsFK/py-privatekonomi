#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Factory(object):
    def __init__(self):
        self._obj = {}

    def get(self, key):
        if key not in self._obj.keys():
            return False
        else:
            return self._obj[key]

    def set(self, key, value):
        print("setting ", key, "to", value)
        self._obj[key] = value

    def getKeys(self):
        return self._obj.keys()

    def getValues(self):
        return self._obj.values()