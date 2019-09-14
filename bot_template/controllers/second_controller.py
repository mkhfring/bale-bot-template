import functools
import os
import sys

from balebot.handlers import MessageHandler
from balebot.filters import TemplateResponseFilter, TextFilter
from balebot.models.messages import TemplateMessage, TemplateMessageButton,\
    TextMessage
import khayyam

from bot_template.utils.mimetype import MimeType
from bot_template.utils.result_writer import ResultWriter
from .root_controller import RootController
from bot_template.bot.constants import ButtonMessage, ConstantMessage, FieldTranslation
from bot_template.database.dbhandler import DB2Handler
from bot_template.config import BotConfig
from bot_template import MAIN_DIRECTORY


RESULT_PATH = os.path.join(MAIN_DIRECTORY, 'data')


class OfficerScoreController(RootController):

    def __init__(self, dispatcher):
        self.dispatcher = dispatcher
        self.handlers = [
            MessageHandler(
                TemplateResponseFilter(ButtonMessage.officer_score_message),
                self.officer_score_initial_state
            )
        ]

    def __call__(self, *args, **kwargs):
        super().__call__()

    def officer_score_initial_state(self, bot, update):
        self.handlers.extend(self.dispatcher.message_handlers)
        user = update.get_effective_user()
        message = TemplateMessage(
            TextMessage(ConstantMessage.report_begin_date_message),
            [
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
                    keywords=[ButtonMessage.main_menu_message]
                ),
                self.show_menu
            ),
        ])
        self.dispatcher.register_conversation_next_step_handler(
            update,
            self.handlers +
            [
                MessageHandler(
                    TextFilter(),
                    self.handle_report_begin_date
                )
            ]
        )

    def create_and_send_final_report(self, update, bot):
        pass
