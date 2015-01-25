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
            return pks[0]
        else:
            return pks

    def get(self, by_col):
        return self.select([self.ref], self.col(by_col) == name)

    def getValue(self, get_value, by_col, where_col):
        return self.selectValue(get_value, self.col(by_col) == where_col)
