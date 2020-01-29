#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
import py_privatekonomi.core.model
import py_privatekonomi.utilities.common
class BaseModel(py_privatekonomi.core.model.Model):
    def __init__(self, ref, context):
        super(BaseModel, self).__init__(context)
        self.ref = ref

    def create(self, data):
        pks =  self.insert(data)
        if len(pks) == 1:
            self.__pks = pks[0]
            return pks[0]
        else:
            self.__pks = pks
            return pks

    def createMany(self, data):
        self.insertMany(data)

    def get(self, by_col = None, where_value = None):
        if by_col is not None and where_value is not None:
            return self.select([self.ref], self.col(by_col) == where_value)
        else:
            return self.select([self.ref])

    def createAndGet(self, data, by_col, check_if_exists = False):
        pks = self.create(data)
        return self.get(by_col, where_value=pks)

    def getValue(self, get_value, by_col, where_col):
        return self.selectValue(get_value, self.col(by_col) == where_col)

    def getResults(self, result_set, cols, decode = False):
        results = []
        for rs in result_set:
            result = {}
            for col in cols:
                result[col] = rs[self.col(col)]
                if decode is True:
                    result[col] = py_privatekonomi.utilities.common.decode(result[col])
            results.append(result)
        return results

    def id(self):
        return self.__pks
