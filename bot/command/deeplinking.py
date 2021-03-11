#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/deeplinking.py
Bot that explains Telegram's "Deep Linking Parameters" functionality.
This program is dedicated to the public domain under the CC0 license.
This Bot uses the Updater class to handle the bot.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Deep Linking example. Send /start to get the link.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, Filters

from telegram.utils import helpers

# Enable logging
logger = logging.getLogger(__name__)

# Define constants that will allow us to reuse the deep-linking parameters.
CHECK_THIS_OUT = "check-this-out"
USING_ENTITIES = "using-entities-here"
SO_COOL = "so-cool"


def start(update, context):
    """Send a deep-linked URL when the command /start is issued."""
    bot = context.bot
    url = helpers.create_deep_linked_url(
        bot.get_me().username, CHECK_THIS_OUT, group=True
    )
    text = "Feel free to tell your friends about it:\n\n" + url
    update.message.reply_text(text)


def deep_linked_level_1(update, context):
    """Reached through the CHECK_THIS_OUT payload"""
    bot = context.bot
    url = helpers.create_deep_linked_url(bot.get_me().username, SO_COOL)
    text = (
        "Awesome, you just accessed hidden functionality! "
        " Now let's get back to the private chat."
    )
    keyboard = InlineKeyboardMarkup.from_button(
        InlineKeyboardButton(text="Continue here!", url=url)
    )
    update.message.reply_text(text, reply_markup=keyboard)


def deep_linked_level_2(update, context):
    """Reached through the SO_COOL payload"""
    bot = context.bot
    url = helpers.create_deep_linked_url(bot.get_me().username, USING_ENTITIES)
    text = (
        "You can also mask the deep-linked URLs as links: "
        "[▶️ CLICK HERE]({0}).".format(url)
    )
    update.message.reply_text(
        text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True
    )


def deep_linked_level_3(update, context):
    """Reached through the USING_ENTITIES payload"""
    payload = context.args
    update.message.reply_text(
        "Congratulations! This is as deep as it gets 👏🏻\n\n"
        "The payload was: {0}".format(payload)
    )


DEEPLINKING_HANDLERS = [
    CommandHandler("deeplinking", deep_linked_level_1, Filters.regex(CHECK_THIS_OUT)),
    CommandHandler("deeplinking", deep_linked_level_2, Filters.regex(SO_COOL)),
    CommandHandler(
        "deeplinking",
        deep_linked_level_3,
        Filters.regex(USING_ENTITIES),
        pass_args=True,
    ),
    CommandHandler("deeplinking", start),
]
