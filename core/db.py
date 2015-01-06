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
    def connect(self):
        db_config = config.readConfig("db", "Database")
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

    def getEngine(self):
        return self.__engine

    def getConnection(self):
        return self.__connection

if __name__ == '__main__':
    db = DB()
    print(sqlalchemy.__version__)
    db.connect()
    db.getEngine()
