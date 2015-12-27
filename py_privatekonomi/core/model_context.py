#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import MetaData
from py_privatekonomi.utilities import common
class ModelContext(object):
    def __init__(self, context = {}):
        self.__context = common.as_obj(context)
        self.__context._metadata = MetaData()

    @property
    def metadata(self):
        return self.__context._metadata

