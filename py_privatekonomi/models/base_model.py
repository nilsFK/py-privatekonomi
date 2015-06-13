#!/usr/bin/env python
# -*- coding: utf-8 -*-
import py_privatekonomi.core.model
class BaseModel(core.model.Model):
    def __init__(self, ref, context):
        super(BaseModel, self).__init__(context)
        self.ref = ref