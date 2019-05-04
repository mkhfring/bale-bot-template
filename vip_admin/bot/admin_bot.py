import asyncio

from balebot.updater import Updater

from vip_admin.config import BotConfig
from vip_admin.bot.controllers import RootController, OfficerScoreController, \
    CustomerController, \
    OfficerSearchController


loop = asyncio.get_event_loop()
updater = Updater(token=BotConfig.token, loop=loop)
dispatcher = updater.dispatcher
RootController(dispatcher)()
OfficerScoreController(dispatcher)()
CustomerController(dispatcher)()
OfficerSearchController(dispatcher)()


if __name__ == '__main__':
    updater.run()

