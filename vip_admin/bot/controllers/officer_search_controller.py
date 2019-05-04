import os
import re
import sys
import functools

import khayyam
from balebot.filters import TemplateResponseFilter, TextFilter
from balebot.handlers import MessageHandler
from balebot.models.messages import TemplateMessage, TextMessage, \
    TemplateMessageButton

from vip_admin.bot.constants import ButtonMessage, ConstantMessage, \
    RegexPattern, FieldTranslation
from vip_admin.config import BotConfig
from vip_admin.database.dbhandler import DB2Handler
from vip_admin.utils.mimetype import MimeType
from vip_admin.utils.result_writer import ResultWriter
from .customer_controller import CustomerController
from vip_admin import MAIN_DIRECTORY


RESULT_PATH = os.path.join(MAIN_DIRECTORY, 'data')


# TODO: Check if it is possible to use some common tasks like handling the branch code as mixin
class OfficerSearchController(CustomerController):

    def __init__(self, dispatcher):
        self.dispatcher = dispatcher
        self.handlers = [
            MessageHandler(
                TemplateResponseFilter(ButtonMessage.officer_search_message),
                self.initiate_search_officers
            )
        ]

    def __call__(self, *args, **kwargs):
        super().__call__()

    def initiate_search_officers(self, bot, update):
        self.handlers.extend(self.dispatcher.message_handlers)
        user = update.get_effective_user()
        message = TemplateMessage(
            TextMessage(ConstantMessage.officer_search_criterion),
            [
                TemplateMessageButton(ButtonMessage.all_officers),
                TemplateMessageButton(ButtonMessage.main_menu_message)
            ]
        )
        self.send_message(
            bot,
            update,
            message,
            user,
            sys._getframe().f_code.co_name
        )
        self.handlers.extend([
            MessageHandler(
                TemplateResponseFilter(
                    keywords=[ButtonMessage.all_officers]
                ),
                self.handle_customer_criterion_input
            ),
            MessageHandler(
                TemplateResponseFilter(
                    keywords=[ButtonMessage.main_menu_message]
                ),
                self.show_menu
            ),
        ])

        # TODO: This seems odd to me to add two lists, find a better way if possible
        self.dispatcher.register_conversation_next_step_handler(
            update,
            self.handlers +
            [
                MessageHandler(
                    TextFilter(),
                    self.handle_customer_criterion_input
                )
            ]
        )

    def create_and_send_final_report(self, update, bot):
        pass
