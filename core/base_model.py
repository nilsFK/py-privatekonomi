#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Use BaseModel for common functionality
import lib.model
class BaseModel(lib.model.Model):
    def __init__(self, ref):
        super(BaseModel, self).__init__()
        self.ref = ref