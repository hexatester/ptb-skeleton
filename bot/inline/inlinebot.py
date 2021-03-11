#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/inlinebot.py
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic inline bot example. Applies different text transformations.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
import logging
from bot.utils.helpers import article
from uuid import uuid4

from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent
from telegram.utils.helpers import escape_markdown

# Enable logging
logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.


def inlinebot(update, context):
    """Handle the inline query."""
    query = update.inline_query.query
    results = [
        article(
            title="Caps",
            description="Caps",
            message_text=InputTextMessageContent(query.upper()),
        ),
        article(
            title="Bold",
            description="Bold",
            message_text=InputTextMessageContent("*{}*".format(escape_markdown(query))),
        ),
        article(
            title="Italic",
            description="Italic",
            message_text=InputTextMessageContent("_{}_".format(escape_markdown(query))),
        ),
    ]
    return results
