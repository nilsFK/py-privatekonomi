#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Use BaseModel for common functionality
import core.model
class BaseModel(core.model.Model):
    def __init__(self, ref):
        super(BaseModel, self).__init__()
        self.ref = ref