import asyncio

from balebot.updater import Updater

from bot_template.config import BotConfig
from bot_template.bot.controllers import RootController, OfficerScoreController, \
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

