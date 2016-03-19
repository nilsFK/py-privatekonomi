#!/usr/bin/env python
# -*- coding: utf-8 -*-
from py_privatekonomi.utilities import helper
from py_privatekonomi.utilities.common import as_obj, is_string
from py_privatekonomi.utilities.proxy import HookProxy
from py_privatekonomi.utilities.models import rebuild_tables, create_tables
from py_privatekonomi.core import loader
from py_privatekonomi.core.error import (MissingAppFunctionError, FormatterError, ParserError)
import py_privatekonomi.core.db
from py_privatekonomi.core.mappers.economy_mapper import EconomyMapper

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

class App(object):
    def __init__(self):
        self.__formatter = None
        self.__parser = None
        self.__sources = []
        self.__persist = False
        self.__config =  {}
        self.__db = {}
        self.__output = None
        self.__auto_discover = False
        self.__discover_from = None
        self.app = None

    def setFormatter(self, formatter_name):
        self.__formatter = formatter_name

    def setParser(self, parser_name):
        self.__parser = parser_name

    def addSource(self, source_name):
        self.__sources.append(source_name)

    def addSources(self, source_names):
        self.__sources.extend(source_names)

    def clearSources(self):
        self.__sources = []

    def persistWith(self, database_settings):
        self.__persist = True
        self.__db = database_settings

    def setOutput(self, output):
        """ Setting the output will avoid calling execute, but
        may still trigger a call to persist.
        If output is set, the building process will not consider
        formatter, parser, or source(s) """
        self.__output = output

    def autodiscover(self, discover_from):
        """ This will attempt to guess the formatter
            and parser given a list of parsers and formatters of format:
            discover_from = [
                {
                    'formatter' : 'swedbank',
                    'parser' : 'swedbank'
                }, { ... }
            ]
        """
        if self.__formatter is not None:
            raise Exception("Unable to autodiscover; Formatter is already set to: %s" % (self.__formatter))
        if self.__parser is not None:
            raise Exception("Unable to autodiscover; Parser is already set to: %s" % (self.__parser))
        self.__auto_discover = True
        self.__discover_from = discover_from

    def config(self, conf):
        self.__config.update(conf)

    def isBuilt(self):
        return self.app is not None

    def __set_parser(self, core):
        self.app['parser'] = None
        if self.__parser is not None:
            self.app['parser'] = self.__load_parser(self.__parser, core)

    def __set_formatter(self, core):
        self.app['formatter'] = None
        if self.__formatter is not None:
            self.app['formatter'] = self.__load_formatter(self.__formatter, core)

    def __load_formatter(self, formatter_name, core):
        return loader.load_formatter(formatter_name, core['factories']['formatters']['account_formatter_factory'])

    def __load_parser(self, parser_name, core):
        return loader.load_parser(parser_name, core['factories']['parsers']['account_parser_factory'])

    def __autodiscover(self, core):
        self.app['formatter'] = None
        self.app['parser'] = None
        for discover in self.__discover_from:
            formatter = self.__load_formatter(discover['formatter'], core)
            if formatter is not None:
                parser = self.__load_parser(discover['parser'], core)
                if parser is not None:
                    self.app['formatter'] = formatter
                    self.app['parser'] = parser
                    return True
        return False

    def _rebuildTables(self, raw_models=None, customizations={}):
        _customizations = {}
        if 'customizations' in self.__config:
            _customizations = self.__config['customizations']
        apply_customizations = _customizations.copy()
        apply_customizations.update(customizations)
        if raw_models is None:
            raw_models = loader.load_models(EconomyMapper.getModelNames())
        return rebuild_tables(raw_models, apply_customizations)

    def _createTables(self, raw_models=None, customizations={}):
        _customizations = {}
        if 'customizations' in self.__config:
            _customizations = self.__config['customizations']
        apply_customizations = _customizations.copy()
        apply_customizations.update(customizations)
        if raw_models is None:
            raw_models = loader.load_models(EconomyMapper.getModelNames())
        return create_tables(raw_models, customizations)

    def build(self):
        self.app = {}
        core = loader.load_core()
        self.app['core'] = core
        if len(self.__db) > 0:
            self.__config['database'] = self.__db
        if self.__output is None and self.__auto_discover is False:
            if self.__formatter is None:
                raise Exception("Formatter has not been specified, please call setFormatter, setOutput, or autodiscover")
            if self.__parser is None:
                raise Exception("Parser has not been specified, please call setParser, setOutput, or autodiscover")
            if len(self.__sources) == 0:
                raise Exception("Sources have not been specified, please call addSource, setOutput, or autodiscover")
            self.__set_parser(self.app['core'])
            self.__set_formatter(self.app['core'])
        elif self.__auto_discover is True:
            found = self.__autodiscover(self.app['core'])
            if not found:
                raise Exception("Unable to find parser/formatter from %s" % (repr(self.__discover_from)))
        if self.__persist is True:
            try:
                customizations = loader.load_customizations(self.__parser)
                self.config({
                    'customizations' : customizations
                })
            except ImportError as e:
                pass
        return self

    def run(self):
        def __execute():
            errors = []
            if self.__auto_discover is True:
                found = False
                for discover in self.__discover_from:
                    try:
                        parser = self.__load_parser(discover['parser'], self.app['core'])
                        formatter = self.__load_formatter(discover['formatter'],  self.app['core'])
                        if parser is None or formatter is None:
                            continue
                        output = self.execute(
                            sources=self.__sources,
                            parser=parser,
                            formatter=formatter,
                            configs=as_obj(self.__config))
                        self.app['parser'] = discover['parser']
                        self.app['formatter'] = discover['formatter']
                        found = True
                        break
                    except FormatterError as e:
                        e_ = repr(e)
                        e_ += "(%s)" % (repr(self.__sources))
                        errors.append(e_)
                        continue
                    except ParserError as e:
                        e_ = repr(e)
                        e_ += "(%s)" % (repr(self.__sources))
                        errors.append(e_)
                        continue
                if found is False:
                    raise Exception("Unable to parse/format using available parsers and formatters from %s (errors=%s)" % (repr(self.__discover_from), repr(errors)))
            else:
                output = self.execute(self.__sources, self.app['parser'], self.app['formatter'], as_obj(self.__config))
            return output

        if self.app is None:
            raise Exception("Build app using app.build() before running.")
        ret = {}
        if self.__output is not None:
            ret['execute'] = self.__output
            ret['formatter'] = 'unknown'
            ret['parser'] = 'unknown'
        else:
            if 'execute' not in dir(self):
                raise MissingAppFunctionError(capture_data={
                    'fun_name' : 'execute',
                    'app' : self.app
                })
            ret['execute'] = __execute()
            if not is_string(self.app['formatter']):
                ret['formatter'] = self.app['formatter'].getName()
            else:
                ret['formatter'] = self.app['formatter']
            if not is_string(self.app['parser']):
                ret['parser'] = self.app['parser'].getName()
            else:
                ret['parser'] = self.app['parser']
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
            ret['persist'] = self.persist(ret['execute'], as_obj(self.__config))
        return ret

    def __repr__(self):
        return "App %s" % (repr(self.__config))
