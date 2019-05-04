import unittest
from datetime import datetime, timedelta

from vip_admin.database.dbhandler import DB2Handler
from vip_admin.config import BotConfig


base_time = datetime.today()-timedelta(2)
start_date = base_time.strftime('%Y-%m-%d') + ' 00:00:00'
end_date = base_time.strftime('%Y-%m-%d') + ' 23:59:00'
schema = 'ACC_OFF'
practice_table = 'account_officers'


class DB2Connection(unittest.TestCase):

    def test_connection(self):
        handler = DB2Handler(
            host=BotConfig.db_hostname,
            port=BotConfig.db_port,
            database=BotConfig.db_name,
            username=BotConfig.db_username,
            password=BotConfig.db_password
        )
        assert isinstance(handler, DB2Handler)
        handler.connect()
        assert handler.connection is not None
