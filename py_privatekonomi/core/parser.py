#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Parser(object):
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name