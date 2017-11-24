#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlalchemy
from sqlalchemy import __version__
from sqlalchemy import create_engine
import sqlalchemy.engine.url as url
# from core import config
from py_privatekonomi.utilities import common
from py_privatekonomi.utilities.common import (singleton, is_dict, is_Struct, as_obj)

@singleton
class DB(object):
    def connect(self, db_config):
        if is_dict(db_config):
            db_config = as_obj(db_config)
        else:
            if not is_Struct(db_config):
                raise Exception("db_config must be either dict or common.Struct: %s" % (repr(db_config)))
        engine_url = url.URL(
            drivername=db_config.engine,
            host=db_config.host,
            port=db_config.port,
            username=db_config.username,
            password=db_config.password,
            database=db_config.database,
            query={ 'charset' : 'utf8' }
        )
        self.__engine = create_engine(engine_url, encoding='utf-8')
        self.__connection = self.__engine.connect()
        self.__config = db_config
        self.__connected = True

    def getEngine(self):
        return self.__engine

    def getConnection(self):
        return self.__connection

    def getConfig(self, config = None):
        if config is not None:
            return getattr(self.__config, config)
        else:
            return self.__config

    def hasConfig(self, config_name):
        return hasattr(self.__config, config_name)

    def isConnected(self):
        try:
            is_connected = self.__connected
        except AttributeError:
            return False
        return is_connected


if __name__ == '__main__':
    db = DB()
    print(sqlalchemy.__version__)
    db.connect()
    db.getEngine()
