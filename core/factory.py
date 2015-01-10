#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Factory(object):
    def __init__(self, obj):
        self._obj = obj

    def get(self, key):
        if key not in self._obj.keys():
            return False
        else:
            return self._obj[key]

    def getTypes(self):
        return self._obj.keys()