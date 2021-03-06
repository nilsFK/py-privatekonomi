#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    A general purpose node containing edges
"""

from __future__ import unicode_literals
class Node(object):
    def __init__(self, name):
        self.name = name
        self.edges = []

    def addEdge(self, node):
        self.edges.append(node)

    def getName(self):
        return self.name