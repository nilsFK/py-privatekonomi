#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Use BaseModel for common functionality
from model import Model
class BaseModel(Model):
    def __init__(self):
        super(BaseModel, self).__init__()