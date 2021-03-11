#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic inline bot example. Applies different text transformations.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
from bot.utils.helpers import article
from uuid import uuid4
from .inlinebot import inlinebot

from telegram.ext import InlineQueryHandler, CommandHandler

# Enable logging
logger = logging.getLogger(__name__)


def inlinequery(update, context):
    query = update.inline_query.query
    results_list = []
    # ... do stuff if length of query > 0
    if len(query) > 0:
        results_list.extend(inlinebot(update, context))
    if not results_list:
        # if no data results_list
        results_list.append(
            article(
                title="Not found. X",
                description="",
                message_text=f"Didnt found anything?",
            )
        )
    update.inline_query.answer(results_list)


HANDLERS = [InlineQueryHandler(inlinequery)]


def register_inlines(dispatcher):
    if HANDLERS:
        for handler in HANDLERS:
            dispatcher.add_handler(handler)
