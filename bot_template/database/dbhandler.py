import os
from datetime import datetime
from urllib.parse import urlparse
from collections import OrderedDict

import ibm_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from balebot.utils.logger import Logger
from bot_template.exeptions import DB2Exception


logger = Logger().get_logger()


class AbstractDBHandler:

    def __init__(self, db_url=None):
        self.db_url = db_url
        self.db_name = urlparse(self.db_url).path.lstrip('/')
        self.engine = create_engine(self.db_url)

    def create_database_if_not_exist(self):
        if self.database_exists():
            self.create_database()

    def database_exists(self):
        raise NotImplemented

    def create_database(self):
        raise NotImplemented

    def get_session(self):
        Session = sessionmaker(bind=self.engine)
        return Session()

    def drop_database(self):
        raise NotImplemented


class SqliteHandler(AbstractDBHandler):

    def __init__(self, url=None):
        super().__init__(url)
        self.filename = self.db_url.replace('sqlite:///', '')

    def database_exists(self):
        return os.path.isfile(self.filename)

    def create_database(self):
        if self.database_exists():
            raise RuntimeError(
                'The file is already exists'
            )
        connection = self.engine.connect()
        connection.close()

    def drop_database(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)


class DB2Handler(AbstractDBHandler):
    def __init__(self, host, port, database, username, password):
        self.host = host
        self.port = port
        self.database = database
        self.username = username
        self.password = password

    def connect(self):

        try:
            connection = ibm_db.connect(
                "DATABASE={};HOSTNAME={};PORT={};PROTOCOL=TCPIP;"
                "UID={};PWD={};" \
                    .format(
                    self.database,
                    self.host,
                    self.port,
                    self.username,
                    self.password
                ), "", ""
            )
        except Exception:
            logger.error(
                'Database Connection Failed',
                extra={
                    'reason': ibm_db.conn_errormsg(),
                    'time': datetime.now()
                }
            )
            raise DB2Exception(ibm_db.conn_errormsg())

        self.connection = connection

    def fetch_statement_data(self, statement):
        self.connect()

        try:
            self.query_result = ibm_db.exec_immediate(
                self.connection,
                statement
            )
        except Exception:
            logger.error(
                'Failed To Execute Query',
                extra={
                    'reason': ibm_db.stmt_errormsg(),
                    'time': datetime.now()
                }
            )
            raise DB2Exception(ibm_db.stmt_errormsg())

        return self._dump_query(self.query_result)

    def _dump_query(self, query):
        result = []
        ibm_fetched_query = ibm_db.fetch_assoc(query)

        while ibm_fetched_query:
            result.append(ibm_fetched_query)
            ibm_fetched_query = ibm_db.fetch_assoc(query)

        return result

