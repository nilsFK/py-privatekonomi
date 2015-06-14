#!/usr/bin/env python
# -*- coding: utf-8 -*-
import loader
from py_privatekonomi.utilities import helper
from py_privatekonomi.utilities.common import as_obj
from py_privatekonomi.utilities.proxy import HookProxy
from py_privatekonomi.core.error import MissingAppFunctionError
import py_privatekonomi.core.db

class AppProxy(HookProxy):
    def __init__(self, objname, obj):
        super(AppProxy, self).__init__(objname, obj)
        self.__called = []

    def _pre( self, name, *args, **kwargs ):
        self.__called.append(name)

    def _post(self, name, *args, **kwargs ):
        pass

    def _pre_run(self, *args, **kwargs ):
        if super(AppProxy, self).getObj().isBuilt() and len(self.__called) > 0:
            if len(self.__called) == 1 and self.__called[0] == 'run':
                return
            raise Exception("Following methods called without building first: %s" % (repr(self.__called)))

    def _post_run(self, *args, **kwargs):
        self.__called = []

    def _post_build(self, *args, **kwargs):
        self.__called = []

    def __repr__(self):
        return super(AppProxy, self).getObj().__repr__()

class App:
    def __init__(self):
        self.__formatter = None
        self.__parser = None
        self.__sources = []
        self.__persist = False
        self.__config =  {}
        self.__db = {}
        self.__output = None
        self.app = None

    def setFormatter(self, formatter_name):
        self.__formatter = formatter_name

    def setParser(self, parser_name):
        self.__parser = parser_name

    def addSource(self, source_name):
        self.__sources.append(source_name)

    def addSources(self, source_names):
        self.__sources.extend(source_names)

    def persistWith(self, database_settings):
        self.__persist = True
        self.__db = database_settings

    def setOutput(self, output):
        """ Setting the output will avoid calling execute, but
        may still trigger a call to persist.
        If output is set, the building process will not consider
        formatter, parser, or source(s) """
        self.__output = output

    def config(self, conf):
        self.__config.update(conf)

    def isBuilt(self):
        return self.app is not None

    def __set_parser(self, core):
        self.app['parser'] = None
        if self.__parser is not None:
            self.app['parser'] = loader.load_parser(self.__parser, core['factories']['parsers']['account_parser_factory'])

    def __set_formatter(self, core):
        self.app['formatter'] = None
        if self.__formatter is not None:
            self.app['formatter'] = loader.load_formatter(self.__formatter, core['factories']['formatters']['account_formatter_factory'])

    def build(self):
        self.app = {}
        core = loader.load_core()
        if len(self.__db) > 0:
            self.__config['database'] = self.__db
        if self.__output is None:
            if self.__formatter is None:
                raise Exception("Formatter has not been specified, please call setFormatter or setOutput")
            if self.__parser is None:
                raise Exception("Parser has not been specified, please call setParser or setOutput")
            if len(self.__sources) == 0:
                raise Exception("Sources have not been specified, please call addSource or setOutput")
        self.app['core'] = core
        self.__set_parser(self.app['core'])
        self.__set_formatter(self.app['core'])
        return self

    def run(self):
        if self.app is None:
            raise Exception("Build app using app.build before running.")
        output = None
        if self.__output is not None:
            output = self.__output
        else:
            if 'execute' not in dir(self):
                raise MissingAppFunctionError(capture_data={
                    'fun_name' : 'execute',
                    'app' : self.app
                })
            output = self.execute(self.__sources, self.app['parser'], self.app['formatter'], as_obj(self.__config))

        if self.__persist is True:
            if 'persist' not in dir(self):
                raise MissingAppFunctionError(capture_data={
                    'fun_name' : 'persist',
                    'app' : self.app
                })
            try:
                py_privatekonomi.core.db.DB().connect(self.__config['database'])
            except AttributeError as e:
                raise Exception("Unable to connect to database: inaccurate database settings.", e)
            self.persist(output, as_obj(self.__config))
        return output

    def __repr__(self):
        return "App %s" % (repr(self.__config))
