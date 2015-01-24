#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import loader
from utilities import common, helper, resolver
from core.node import Node
from core.models.account import Account
from core.models.account_category import AccountCategory
from core.models.organization import Organization
from core.models.provider import Provider
from core.models.transaction import Transaction
from core.models.transaction_type import TransactionType
from core.models.transaction_category import TransactionCategory
from core.models.currency import Currency
from core.models.security import Security
from core.model_context import ModelContext
import core.db
class TestUtilities(unittest.TestCase):
    def setUp(self):
        self.model_types = [
            Account,
            Provider,
            Organization,
            Currency,
            TransactionCategory,
            AccountCategory,
            TransactionType,
            Transaction,
            Security
        ]

    def test_resolver_resolve_dependecy_graph(self):
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')
        e = Node('e')
        e = Node('e')
        a.addEdge(b)
        a.addEdge(d)
        b.addEdge(c)
        b.addEdge(e)
        c.addEdge(d)
        c.addEdge(e)

        resolved = []
        resolver.dependency_resolve(a, resolved, [])
        self.assertEquals(resolved[0].name, "d")
        self.assertEquals(resolved[1].name, "e")
        self.assertEquals(resolved[2].name, "c")
        self.assertEquals(resolved[3].name, "e")
        self.assertEquals(resolved[4].name, "b")
        self.assertEquals(resolved[5].name, "d")
        self.assertEquals(resolved[6].name, "a")

    def test_model_resolver_resolveObliteration(self):
        core.db.DB().connect()

        deps = resolver.getModelDependencies(self.model_types)
        obliteration_order = resolver.resolveObliteration(deps)
        self.assertEquals(len(self.model_types), len(obliteration_order))
        """
        resolution order can variate, so no asserts for now
        """

    def test_model_resolver_resolveGeneration(self):
        core.db.DB().connect()

        deps = resolver.getModelDependencies(self.model_types)
        generation_order = resolver.resolveGeneration(deps)
        self.assertEquals(len(self.model_types), len(generation_order))
        """
        resolution order can variate, so no asserts for now
        """

if __name__ == '__main__':
    unittest.main()