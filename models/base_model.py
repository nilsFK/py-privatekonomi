#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Use BaseModel for common functionality
import core.model
class BaseModel(core.model.Model):
    def __init__(self, ref, context):
        super(BaseModel, self).__init__(context)
        self.ref = ref