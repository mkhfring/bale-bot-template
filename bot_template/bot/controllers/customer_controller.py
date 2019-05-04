import sys
import os
import re
import functools

from balebot.handlers import MessageHandler
from balebot.models.messages import TemplateMessage, TextMessage, \
    TemplateMessageButton
from balebot.filters import TemplateResponseFilter, TextFilter
from balebot.utils.util_functions import arabic_to_eng_number
import khayyam

from bot_template.config import BotConfig
from bot_template import MAIN_DIRECTORY
from bot_template.bot.constants import ConstantMessage, RegexPattern
from bot_template.bot.constants import ButtonMessage
from ..controllers import RootController

supported_users = BotConfig.supported_users
RESULT_PATH = os.path.join(MAIN_DIRECTORY, 'data')


class CustomerController(RootController):

    def __init__(self, dispatcher):
        self.dispatcher = dispatcher
        self.handlers = [
            MessageHandler(
                TemplateResponseFilter(ButtonMessage.customer_search_message),
                self.initiate_search_customer
            )
        ]

    def __call__(self, *args, **kwargs):
        super().__call__()

    @staticmethod
    def check_national_code(code):
        if code.replace("0", "") == "":
            return False

        if 8 <= len(code) <= 10:
            code = '00' + code
            code = code[len(code) - 10:]

            i = 2
            k = 0
            for c in code[-2::-1]:
                k += int(c) * i
                i += 1
            remain = k % 11
            if remain < 2:
                pass
            else:
                remain = 11 - remain

            if remain == int(code[-1]):
                return True
            else:
                return False

        else:
            return False

    def initiate_search_customer(self, bot, update):
        self.handlers.extend(self.dispatcher.message_handlers)
        user = update.get_effective_user()
        message = TemplateMessage(
            TextMessage(ConstantMessage.customer_search_criterion),
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

    # TODO: change to names to be more general in order to use in office search as well
    def handle_customer_criterion_input(self, bot, update):
        user = update.get_effective_user()
        message = arabic_to_eng_number(update.get_effective_message().text)
        if message != ButtonMessage.all_officers:
            self.dispatcher.set_conversation_data(
                update=update,
                key='officer_criterion',
                value=message
            )

        message = TemplateMessage(
            TextMessage(ConstantMessage.report_begin_date_message),
            [TemplateMessageButton(ButtonMessage.main_menu_message)]
        )
        self.send_message(
            bot,
            update,
            message,
            user,
            sys._getframe().f_code.co_name
        )
        self.dispatcher.register_conversation_next_step_handler(
            update,
            self.handlers +
            [
                MessageHandler(TextFilter(), self.handle_report_begin_date),
            ]
        )

    def create_and_send_final_report(self, update, bot):
        pass
