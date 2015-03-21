#!/usr/bin/env python
# -*- coding: utf-8 -*-
import utilities.models as models_utility
from utilities.models import get_table_name
from utilities import common
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

    def fillDataGap(self, model, data):
        table_name = self._models.asTableName(model)
        model_name = models_utility.get_model_name(table_name)
        self._filler_data[table_name] = data
        if table_name not in self._inserted:
            self._inserted[table_name] = []
        self.__insert(table_name, data)

    def useLogging(self, use):
        self._use_log = use

    def persist(self, content):
        dependency_order = models_utility.get_dependency_order(self._models.all())

        self._model_data = {}
        for model_name in self._models.internal():
            value = self._models.internal()[model_name]
            self._log(model_name)
            data = {}
            data["model_struct"] = value
            data["model_name"] = model_name
            data["table_name"] = models_utility.get_table_name(model_name)
            data["model_type"] = type(value)
            self._model_data[data["model_name"]] = data
            if data["table_name"] not in self._inserted:
                self._inserted[data["table_name"]] = []

        self.__callback("_before_process")

        for data in content:
            resolved_row = []
            resolved_dependency_data = {} # <-- resolved so far in the dependency order
            for model_name in dependency_order:
                self._log(("storing", model_name))
                self._log("dependency_data:", repr(resolved_dependency_data))

                model_data = data[model_name] if model_name in data else None
                resolved_row = getattr(self, "_resolve_%s" % self._model_data[model_name]["table_name"])(model_data, resolved_dependency_data)
                if isinstance(resolved_row, list) and len(resolved_row) == 1:
                    resolved_row = resolved_row[0]
                resolved_dependency_data[model_name] = resolved_row

                self.__buffer_store(model_name, resolved_row)
                self.__resolve_buffers(model_name, False)
                self._log("-"*40)
            self._log("="*40)

        self.__callback("_after_process")

        # Is there anything else left to resolve?
        self._log("="*80)
        self._log("we have now analyzed all data, let's resolve remaining buffers if any")
        for idx, model_name in enumerate(dependency_order):
            if model_name == 'Transaction':
                self.__resolve_buffers(dependency_order[idx], True)
                break

        self._log("***** DONE! *****")

    def _log(self, *msg):
        if self._use_log is True:
            for m in msg:
                print(m)

    def _hasFiller(self, model):
        return self._models.asTableName(model) in self._filler_data

    def __insert(self, table, data):
        if isinstance(data, dict):
            data = [data]
        insertion_point = self._inserted[table]
        insertion_point.extend(data)

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
        self._log("Hello, I am " + table_name + " and I depend on " + repr(i_depend_on))
        self._log("Buffer stored: " + str(buffer_stored))
        self._log("Buffer capacity: " + str(buffer_capacity))
        self._log("Force resolve: " +  str(force_resolve))

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

    def __is_inserted(self, table_name, by_key, by_val):
        if by_key is None or by_val is None:
            return False
        insertion_point = self._inserted[table_name]
        for ins in self._inserted[table_name]:
            if by_key in ins and common.unicode(common.decode(ins[by_key])) == common.unicode(by_val):
                return True
        return False

    def __persist(self, table_name):
        if "_persist_%s" % table_name in dir(self):
            return self.__callback("_persist_%s" % table_name)
        persist_data = self.__buffer.get(table_name)[0]
        self._log("!"*80)
        self._log("Persisting: " + table_name + " " +  repr(persist_data))
        self._log("!"*80)

        id_key = None
        id_val = None

        # Test in order of accepted keys
        # TODO: Generate the names of the keys somewhere else, before resolving
        valid_ins_keys = ["id", "name", "code"]
        for vis in valid_ins_keys:
            if id_key is not None: break
            elif isinstance(persist_data, list):
                for pdata in persist_data:
                    if vis in pdata:
                        id_key = vis
                        id_val = pdata[id_key]
                        break
            elif isinstance(persist_data, dict):
                if vis in persist_data:
                    id_key = vis
                    id_val = persist_data[vis]
                    break
            else:
                raise Exception("Invalid datatype given for persist_data: " + type(persist_data))

        self._log("decided that identifier key was: " + repr(id_key))
        self._log("decided that identifier val was: " + repr(id_val))

        is_inserted = self.__is_inserted(table_name, id_key, id_val)

        if not is_inserted:
            self._log("persisting...")
            row_id = self._model_data[models_utility.get_model_name(table_name)]["model_struct"].create(persist_data)
            if "id" not in persist_data:
                persist_data["id"] = row_id
            self.__insert(table_name, persist_data)
        else:
            self._log("This has already been inserted")

        self._log(self._inserted[table_name])

        self._log("Clearing buffer storage for", table_name)
        self.__buffer.clear_storage(table_name)

    def __callback(self, name):
        if name in dir(self):
            return getattr(self, name)()
