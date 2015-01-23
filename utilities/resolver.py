#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core.model_context import ModelContext
from core.models.account import Account
from core.models.account_category import AccountCategory
from core.node import Node

def getModelDependencies(model_types):
    dependencies = {}
    context = ModelContext()
    nodes = {}
    models = []
    for model_type in model_types:
        _model = model_type(context)
        nodes[_model.getName()] = Node(_model.getName())
        models.append(_model)

    for node_key, node_val in nodes.iteritems():
        print node_key

    for model in models:
        fks = model.getForeignKeys(model.getName())
        for fk in fks:
            print(repr(fk))
            print "-"*80
            nodes[model.getName()].addEdge(nodes[fk['referred_table']])

    for node_key, node_val in nodes.iteritems():
        resolved = []
        print "resolving: " + node_key
        print "="*80
        dependency_resolve(node_val, resolved, [])
        dependencies[node_key] = []
        for res in resolved:
            dependencies[node_key].append(res.getName())
        print "-"*80
    return dependencies

def dependency_resolve(node, resolved, unresolved):
    unresolved.append(node)
    for edge in node.edges:
        if edge in unresolved:
            raise Exception("Circular reference: %s->%s" %
                (node.name, edge.name))
        dependency_resolve(edge, resolved, unresolved)
    resolved.append(node)
    unresolved.remove(node)

def resolveObliteration(dependencies):
    obliterated = []
    def __depends_on_me(me):
        depends_on_me = set()
        for them, deps in dependencies.iteritems():
            if me in deps and them is not me:
                if them not in obliterated:
                    depends_on_me.add(them)
        ret = list(depends_on_me)
        return ret if len(depends_on_me) > 0 else None
    def __resolve(me):
        if me in obliterated:
            print "Hey, I'm " + me + " and I'm already dead :\\"
            return
        print "resolve " + me
        print "look for those who depend on me:"
        depends_on_me = __depends_on_me(me)
        print repr(depends_on_me)
        if depends_on_me is None:
            print "Oh noes! no one depends on me. commit suicide =("
            obliterated.append(me)
        else:
            print "Some depend on me. Let's destroy them!"
            for destroy_them in depends_on_me:
                __resolve(destroy_them)
        print "*"*80
    for dep in dependencies:
        __resolve(dep)
    print "="*80
    print "obliteration resolution"
    print repr(obliterated)
    return obliterated

def resolveGeneration(dependencies):
    obliterated = resolveObliteration(dependencies)
    return obliterated.reverse()