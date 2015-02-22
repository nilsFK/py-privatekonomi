#!/usr/bin/env python
# -*- coding: utf-8 -*-
import utilities.models as models_utility
from utilities.models import get_table_name
from utilities import common
from sys import exit
import sys
from core.buffer import Buffer
from core.model_container import ModelContainer

"""
    A base class for resolving models and persisting data to database
"""

class Persist(object):
    def __init__(self, models):
        self.__dependencies = models_utility.get_model_dependencies_struct(models)
        self._filler_data = {}
        self.__buffer = Buffer()
        self._models = ModelContainer(models)
        self._inserted = {}
        self._use_log = False

    def buffer(self, model, n):
        self.__buffer.buffer(self._models.asTableName(model), n)

    def fillDataGap(self, model, data):
        table_name = self._models.asTableName(model)
        model_name = models_utility.get_model_name(table_name)
        self._filler_data[table_name] = data
        if table_name not in self._inserted:
            self._inserted[table_name] = []
        # print(repr(table_name))
        # print(repr(data))
        # print(repr(self._inserted))
        self.__insert(table_name, data)

    def __insert(self, table, data):
        known_identifiers = ["id", "name", "code"]
        insertion_point = self._inserted[table]
        self._log("Inserting data:")
        self._log(table, data)
        self._log("inserted for " + table + " at this point:")
        self._log(insertion_point)

        insertion_point.append(data)

    def __is_inserted(self, table_name, by_key, by_val):
        self._log("__is_inserted")
        insertion_point = self._inserted[table_name]
        self._log("rummaging through:")
        self._log(insertion_point)
        for next_ins in self._inserted[table_name]:
            self._log("comparing " + repr(common.unicode(common.decode(next_ins[by_key])))
                + " with " + repr(common.unicode(by_val)))
            if by_key in next_ins and common.unicode(common.decode(next_ins[by_key])) == common.unicode(by_val):
                return True
        return False


    def useLogging(self, use):
        self._use_log = use

    def persist(self, content):
        self._log("initial inserted data:")
        self._log(self._inserted)
        dependency_order = models_utility.get_dependency_order(self._models.all())

        self._model_data = {}
        for model_name, value in self._models.internal().iteritems():
            self._log(model_name)
            data = {}
            data["model_struct"] = value
            data["model_name"] = model_name
            data["table_name"] = models_utility.get_table_name(model_name)
            data["model_type"] = type(value)
            self._model_data[data["model_name"]] = data
            if data["table_name"] not in self._inserted:
                self._inserted[data["table_name"]] = []

        for data in content:
            resolved_row = []
            resolved_dependency_data = {} # <-- resolved so far in the dependency order
            for model_name in dependency_order:
                self._log(("storing", model_name))
                self._log("dependency_data:", repr(resolved_dependency_data))

                model_data = data[model_name] if model_name in data else None
                resolved_row = getattr(self, "_resolve_%s" % self._model_data[model_name]["table_name"])(model_data, resolved_dependency_data)
                resolved_dependency_data[model_name] = resolved_row

                self.__buffer_store(model_name, resolved_row)
                self.__resolve_buffers(model_name, False)
                self._log("-"*40)
            self._log("="*40)
        # Is there anything else left to unbuffer?
        self._log("="*80)
        self._log("we have now analyzed all data, let's resolve remaining buffers if any")
        self.__resolve_buffers(dependency_order[-1], True)
        self._log("***** DONE! *****")

    def _log(self, *msg):
        if self._use_log is True:
            for m in msg:
                print m

    def _hasFiller(self, model):
        return self._models.asTableName(model) in self._filler_data

    def __buffer_store(self, model_name, model_data):
        self.__buffer.store(self._models.asTableName(model_name), model_data)

    def __build_dependencies(self, table_name, dependencies):
        deps = set()
        for dep_table, dep_table_depends_on in dependencies.iteritems():
            if table_name != dep_table and table_name in dep_table_depends_on:
                deps.add(dep_table)
        return list(deps)

    def __resolve_buffers(self, model_name, force_resolve):
        table_name = self._models.asTableName(model_name)
        buffer_stored = self.__buffer.stored(table_name)
        buffer_capacity = self.__buffer.capacity(table_name)
        i_depend_on = self.__dependencies[table_name]
        depends_on_me = self.__build_dependencies(table_name, self.__dependencies)
        self._log("Hello, I am " + table_name + " and I depend on " + repr(i_depend_on))
        self._log("Buffer stored: " + str(buffer_stored))
        self._log("Buffer capacity: " + str(buffer_capacity))
        self._log("Force resolve: " +  str(force_resolve))
        self._log("Who depends on me?: " + repr(depends_on_me))
        dependant_buffers = False
        for dep in depends_on_me:
            if self.__buffer.has(dep):
                self._log(dep + " has buffers")
                dependant_buffers = True
                break
        if depends_on_me is not None and len(depends_on_me) > 0:
            self._log("Do they have buffers?: " + str(dependant_buffers))

        if force_resolve:
            resolve = True
        else:
            resolve = ((buffer_stored == 0 and buffer_capacity == 0) \
                or buffer_stored >= buffer_capacity)
        self._log("Should we resolve? " + str(resolve))

        if resolve is True:
            self._log(">"*40)
            self._log("I will force resolve those i depend on before resolving myself")
            for dependency in i_depend_on:
                self.__resolve_buffers(dependency, True)
            self._log("Control has been given back to: " + table_name)
            self._log("<"*40)
            if self.__buffer.has(table_name) and buffer_stored > 0:
                self.__persist(table_name)
            else:
                self._log("Well, I don't have anything to persist. Next.")

    def __persist(self, table_name):
        persist_data = self.__buffer.get(table_name)[0]
        self._log("!"*80)
        self._log("Persisting: " + table_name + " " +  repr(persist_data))
        self._log("!"*80)

        id_key = None
        id_val = None

        # Test in order of accepted keys
        # TODO: Generate the names of the keys somewhere else, before resolving
        valid_ins_keys = ["id", "name", "code"]

        for v in valid_ins_keys:
            self._log(v)
            if v in persist_data:
                id_key = v
                id_val = persist_data[v]
                break

        self._log("decided that identifier key was: " + repr(id_key))
        self._log("decided that identifier val was: " + repr(id_val))
        self._log("inserted to table before persisting:")

        if id_key is None or id_val is None:
            is_inserted = False
        else:
            is_inserted = self.__is_inserted(table_name, id_key, id_val)
        if not is_inserted:
            self._log("persisting...")
            row_id = self._model_data[models_utility.get_model_name(table_name)]["model_struct"].create(persist_data)
            if "id" not in persist_data:
                persist_data["id"] = row_id
            self.__insert(table_name, persist_data)
        else:
            self._log("This has already been created/inserted")

        self._log(self._inserted[table_name])

        self._log("Clearing buffer storage for", table_name)
        self.__buffer.clear_storage(table_name)