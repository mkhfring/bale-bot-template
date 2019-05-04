import pytest

from vip_admin.database.dbhandler import DB2Handler
from vip_admin.config import BotConfig


@pytest.fixture(scope='module')
def handler():
    handler = DB2Handler(
        host=BotConfig.db_hostname,
        port=BotConfig.db_port,
        database=BotConfig.db_name,
        username=BotConfig.db_username,
        password=BotConfig.db_password
    )
    return handler
