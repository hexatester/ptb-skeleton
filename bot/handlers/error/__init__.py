from bot import logging
from telegram.error import (TelegramError, Unauthorized, BadRequest,
                            TimedOut, ChatMigrated, NetworkError)
from .badrequest import badrequest
from .chatmigrated import chatmigrated
from .networkerror import networkerror
from .telegramerror import telegramerror
from .timedout import timedout
from .unauthorized import unauthorized

logger = logging.getLogger(__name__)


def error(update, context):
    """Log Errors caused by Updates."""
    # https://github.com/python-telegram-bot/python-telegram-bot/wiki/Exception-Handling
    try:
        raise context.error
    except Unauthorized as e:
        # remove update.message.chat_id from conversation list
        unauthorized(update, context, e)
    except BadRequest as e:
        # handle malformed requests - read more below!
        badrequest(update, context, e)
    except TimedOut as e:
        # handle slow connection problems
        timedout(update, context, e)
    except NetworkError as e:
        # handle other connection problems
        networkerror(update, context, e)
    except ChatMigrated as e:
        # the chat_id of a group has changed, use e.new_chat_id instead
        chatmigrated(update, context, e)
    except TelegramError as e:
        # handle all other telegram related errors
        telegramerror(update, context, e)
    logger.warning('Update "%s" caused error "%s"', update, context.error)


HANDLERS = [error]


def register_errors(dispatcher):
    if HANDLERS:
        for handler in HANDLERS:
            dispatcher.add_error_handler(handler)
