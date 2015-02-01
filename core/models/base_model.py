#!/usr/bin/env python
# -*- coding: utf-8 -*-
import core.model
class BaseModel(core.model.Model):
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

    def get(self, by_col, where_value):
        return self.select([self.ref], self.col(by_col) == where_value)

    def createAndGet(self, data, by_col):
        pks = self.create(data)
        return self.get(by_col, where_value=pks)

    def getValue(self, get_value, by_col, where_col):
        return self.selectValue(get_value, self.col(by_col) == where_col)

    def getResults(self, result_set, cols):
        results = []
        for rs in result_set:
            result = {}
            for col in cols:
                result[col] = rs[self.col(col)]
            results.append(result)
        return results

    def id(self):
        return self.__pks

