#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlalchemy
from sqlalchemy import __version__
from sqlalchemy import create_engine
import config
from utilities import common
from utilities.common import singleton

@singleton
class DB(object):
    def connect(self, file_config = "db"):
        db_config = config.readConfig(file_config, "Database")
        db_config = common.as_obj(db_config)
        self.__engine = sqlalchemy.create_engine("%(engine)s://%(username)s:%(password)s@%(host)s:%(port)s/%(database)s" % {
            'engine' : db_config.engine,
            'username' : db_config.username,
            'password' : db_config.password,
            'host' : db_config.host,
            'port' : db_config.port,
            'database' : db_config.database
        })
        self.__connection = self.__engine.connect()
        self.__config = db_config

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


if __name__ == '__main__':
    db = DB()
    print(sqlalchemy.__version__)
    db.connect()
    db.getEngine()
