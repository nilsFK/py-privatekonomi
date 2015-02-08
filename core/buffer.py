#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import MetaData
from utilities import common

"""
A buffering class
"""
class Buffer(object):
    def __init__(self):
        self.__buffer_capacity = {}
        self.__buffer_storage = {}

    def buffer(self, name, n):
        """ How many inserts should be buffered at a time?
        Decided by n.
        """
        if n < 0: n = 0
        self.__buffer_capacity[name] = n
        self.__buffer_storage[name] = []

    def store(self, name, data):
        """ if the buffer is missing we will allocate
        an empty one that has a capacity of 0
        """
        print "Can we buffer:", repr(data)
        if data is not None:
            if not self.has(name):
                self.clear_storage(name)
                self.clear_capacity(name)
            self.__buffer_storage[name].append(data)

    def stored(self, name):
        if self.has(name):
            return len(self.__buffer_storage[name])
        else:
            return 0

    def capacity(self, name):
        if self.has(name):
            return self.__buffer_capacity[name]
        else:
            return 0

    def has(self, name):
        return name in self.__buffer_storage

    def resolveBuffer(self):
        """ to be implemented """
        pass

    def get(self, name):
        return self.__buffer_storage[name]

    def clear_storage(self, name):
        self.__buffer_storage[name] = []

    def clear_capacity(self, name):
        self.__buffer_capacity[name] = 0
