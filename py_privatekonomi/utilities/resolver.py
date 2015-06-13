#!/usr/bin/env python
# -*- coding: utf-8 -*-
from py_privatekonomi.core.model_context import ModelContext
from py_privatekonomi.core.node import Node

def getModelDependencies(model_types):
    context = ModelContext()
    ret_model_deps = {}
    for model_type in model_types:
        _model = model_type(context)
        deps = _model.getDependencies()
        if len(deps) > 0:
            ret_model_deps[_model.getName()] = []
            for dep in deps:
                ret_model_deps[_model.getName()].append(dep["referenced_table"])
        else:
            ret_model_deps[_model.getName()] = []
    return ret_model_deps

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
    """ resolve those who depend on me """
    obliterated = []
    def __obliterate(me):
        if me not in obliterated:
            obliterated.append(me)
    def __depends_on(me):
        depends_on_me = set()
        for them in dependencies:
            deps = dependencies[them]
            if me in deps and them is not me:
                if them not in obliterated:
                    depends_on_me.add(them)
        ret = list(depends_on_me)
        return ret if len(depends_on_me) > 0 else None
    def __resolve(me):
        if me in obliterated:
            """ Hey, I'm me and I'm already dead :\\ """
            return
        """ look for those who depend on me """
        depends_on_me = __depends_on(me)
        if depends_on_me is not None:
            """ Some guys depend on me. Let's destroy them! """
            for destroy_them in depends_on_me:
                __resolve(destroy_them)
        """ well, no one depends on me. commit suicide =( """
        __obliterate(me)
    for some_guy in dependencies:
        __resolve(some_guy)
    return obliterated

def resolveGeneration(dependencies):
    """ resolve those who i depend on """
    generated = []
    def __append(me):
        if me not in generated:
            generated.append(me)
    def __resolve(me, my_dependencies):
        if len(my_dependencies) == 0:
            """ i dont depend on anyone really """
            __append(me)
            return
        """ resolve those who i depend on before i resolve myself """
        for them in my_dependencies:
            __resolve(them, dependencies[them])
        """ now i have resolved my friends, so resolve myself """
        __append(me)
    for some_guy in dependencies:
        their_dependencies = dependencies[some_guy]
        __resolve(some_guy, their_dependencies)
    return generated
