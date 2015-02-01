#!/usr/bin/env python
# -*- coding: utf-8 -*-
import utilities.models as models_utility
from utilities.models import get_table_name
from utilities import common
from sys import exit
import sys
"""
    A base class for resolving models
"""

orig_stdout = sys.stdout
f = file("C:\\Users\\nils\\Desktop\\out.txt", "w")
sys.stdout = f

class Persist(object):
    def __init__(self, models):
        self._models = models
        self.__dependencies = models_utility.get_model_dependencies_struct(self._models)
        self._filler_data = {}
        self.__buffer_capacity = {}
        self.__buffer_storage = {}
        self._inserted_ids = {}

    def buffer(self, model, n):
        """
        How many inserts should be buffered at a time
        before persisting to database? Decided by n.
        """
        if n < 1: n = 1
        self.__buffer_capacity[model.getNormalizedName()] = n
        self.__buffer_storage[model.getNormalizedName()] = []

    def __buffer_store(self, model_name, model_data):
        print "Can we buffer:", repr(model_data)
        if model_data is not None:
            table_name = get_table_name(model_name)
            if table_name not in self.__buffer_storage:
                self.__buffer_storage[table_name] = []
            self.__buffer_storage[table_name].append(model_data)
            print("Buffered", table_name, "to", len(self.__buffer_storage[table_name]))
            print("Buffer now contains:", repr(self.__buffer_storage[table_name]))

    def __check_dependencies(self, table_name, dependencies):
        deps = set()
        for dep_table, dep_table_depends_on in dependencies.iteritems():
            if table_name != dep_table and table_name in dep_table_depends_on:
                deps.add(dep_table)
        return list(deps)

    def __resolve_buffers(self, model_name, force_resolve):
        table_name = get_table_name(model_name)
        buffer_stored = len(self.__buffer_storage[table_name]) if table_name in self.__buffer_storage else 0
        buffer_capacity = self.__buffer_capacity[table_name] if table_name in self.__buffer_capacity else 0
        i_depend_on = self.__dependencies[table_name]
        depends_on_me = self.__check_dependencies(table_name, self.__dependencies)
        print "Hello, I am", table_name
        print "I depend on:", repr(i_depend_on)
        print "Buffer stored:", buffer_stored
        print "Buffer capacity:", buffer_capacity
        print "Force resolve:", force_resolve
        print "Who depends on me?:", repr(depends_on_me)
        dependant_buffers = False
        for dep in depends_on_me:
            if dep in self.__buffer_storage:
                print dep, "has buffers"
                dependant_buffers = True
                break
        if depends_on_me is not None and len(depends_on_me) > 0:
            print "Do they have buffers?:", dependant_buffers
            pass
        if force_resolve:
            resolve = True
        else:
            resolve = ((buffer_stored == 0 and buffer_capacity == 0) \
                or buffer_stored >= buffer_capacity)
        print "Should we resolve?", resolve

        if resolve is True:
            print ">"*40
            print "I will force resolve those i depend on before resolving myself"
            for dependency in i_depend_on:
                self.__resolve_buffers(dependency, True)
            print "Control has been given back to:", table_name
            print "<"*40
            if table_name in self.__buffer_storage and \
                buffer_stored > 0:
                self.__persist(table_name)
            else:
                print "Well, I don't have anything to persist. Next."
                pass
        # exit(1)

    def _hasFiller(self, model):
        return model.getNormalizedName() in self._filler_data

    def __persist(self, table_name):
        print "!"*80
        print("Persisting:", table_name, repr(self.__buffer_storage[table_name]))
        print "!"*80
        print(repr(self._inserted_ids[table_name]))
        persist_data = self.__buffer_storage[table_name]
        if ("id" in persist_data[0] and persist_data[0]["id"] not in self._inserted_ids[table_name]) \
            or ("id" not in persist_data[0]):
                id_ = self._model_data[models_utility.get_model_name(table_name)]["model_struct"].create(persist_data)
                self._inserted_ids[table_name].add(id_)
        else:
            print "This has already been created"
            pass
        print "Clearing buffer storage for", table_name

        self.__buffer_storage[table_name] = []
        if "id" in persist_data[0] and persist_data[0]["id"] not in self._inserted_ids[table_name]:
            self._inserted_ids[table_name].add(persist_data[0]["id"])

    def fillDataGap(self, model, data):
        table_name = model.getNormalizedName()
        model_name = models_utility.get_model_name(table_name)
        self._filler_data[table_name] = data
        if table_name not in self._inserted_ids:
            self._inserted_ids[table_name] = set()
        self._inserted_ids[table_name].add(data["id"])

    def persist(self, content):
        generated_data = {}
        dependency_order = models_utility.get_dependency_order(self._models)

        self._model_data = {}
        for model, value in common.as_dict(self._models).iteritems():
            print model
            data = {}
            data["model_struct"] = value
            data["model_name"] = model
            data["table_name"] = models_utility.get_table_name(model)
            data["model_type"] = type(value)
            self._model_data[data["model_name"]] = data
            if models_utility.get_table_name(model) not in self._inserted_ids:
                self._inserted_ids[models_utility.get_table_name(model)] = set()

        print(repr(dependency_order))
        for model_name in dependency_order:
            generated_data[model_name] = []
        for data in content:
            resolved_row = []
            resolved_dependency_data = {} # <-- resolved so far in the dependency order
            for model_name in dependency_order:
                print ("storing", model_name)
                print("dependency_data:", repr(resolved_dependency_data))
                model_data = data[model_name] if model_name in data else None
                resolved_row = getattr(self, "_resolve_%s" % self._model_data[model_name]["table_name"])(model_data, resolved_dependency_data)
                generated_data[model_name].append(resolved_row)
                resolved_dependency_data[model_name] = resolved_row
                self.__buffer_store(model_name, resolved_row)
                self.__resolve_buffers(model_name, False)
                print "-"*40
            print "="*40
        # Is there anything else left to unbuffer?
        print "="*80
        print "we have now analyzed all data, let's resolve remaining buffers if any"
        self.__resolve_buffers(dependency_order[-1], True)
        print "***** DONE! *****"
        sys.stdout = orig_stdout
        f.close()
