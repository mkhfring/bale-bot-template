import argparse

from  sqlalchemy import create_engine

from vip_admin.database.databasemanager import DatabaseManager
from ..bot.admin_bot import updater
from vip_admin.database import BaseModel
from vip_admin.config import BotConfig


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("square",
                        help="display a square of a given number")
    parser.add_argument("-c", "--create", action="store_true",
                        help="increase output verbosity")
    args = parser.parse_args()
    if args.square == 'start':
        updater.run()

    if args.square == 'db':
        if args.create:
            engine = create_engine(BotConfig.database_url)
            BaseModel.metadata.create_all(engine)


