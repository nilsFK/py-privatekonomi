#!/usr/bin/env python
# -*- coding: utf-8 -*-
import loader
from py_privatekonomi.utilities import helper
from py_privatekonomi.utilities.common import as_obj
from py_privatekonomi.utilities.proxy import HookProxy
import sys

class AppProxy(HookProxy):
    def __init__(self, objname, obj):
        super(AppProxy, self).__init__(objname, obj)
        self.__called = []

    def _pre( self, name, *args, **kwds ):
        self.__called.append(name)

    def _post(self, name, *args, **kwds ):
        pass

    def _pre_run(self, *args, **kwds ):
        if super(AppProxy, self).getObj().isBuilt() and len(self.__called) > 0:
            if len(self.__called) == 1 and self.__called[0] == 'run':
                return
            raise Exception("Following methods called without building: %s" % (repr(self.__called)))

    def _post_run(self, *args, **kwds):
        self.__called = []

    def _post_build(self, *args, **kwargs):
        self.__called = []

class App:
    def __init__(self):
        self.__formatter = None
        self.__parser = None
        self.__source = None
        self.__persist = False
        self.__config =  {}
        self.__db = {}
        self.app = None

    def setFormatter(self, formatter_name):
        self.__formatter = formatter_name

    def setParser(self, parser_name):
        self.__parser = parser_name

    def setSource(self, source_name):
        self.__source = source_name

    def persistWith(self, database_settings):
        self.__persist = True
        self.__db = database_settings

    def config(self, conf):
        self.__config.update(conf)

    def isBuilt(self):
        return self.app is not None

    def build(self):
        if self.__formatter is None:
            raise Exception("Formatter has not been specified")
        if self.__parser is None:
            raise Exception("Parser has not been specified")
        if self.__source is None:
            raise Exception("Source has not been specified")
        if len(self.__db) > 0:
            self.__config['database'] = self.__db

        internal_app = "py_privatekonomi.core.apps.default"
        if self.__persist is True:
            internal_app = "py_privatekonomi.core.apps.example4"
        self.app = loader.load_app(internal_app, self.__source, self.__parser, self.__formatter, self.__persist)
        return self

    def run(self):
        if self.app is None:
            raise Exception("Build app using app.build before running")
        return helper.execute_app(self.app, as_obj(self.__config))

    def __repr__(self):
        return "App %s" % (repr(self.__config))
