#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.
from telegram.ext import CommandHandler


def start(update, context):
    """Send a message when the command /start is issued."""
    msg = [
        "Hi! Use /help to show Help!",
        "/deeplinking to try deep linking"
        "\nhttps://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/deeplinking.py",
        "/inlinekeyboard to try inline keyboard using CallbackQueryHandler"
        "\nhttps://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/inlinekeyboard.py",
        "/inlinekeyboard2 to try inline keyboard using CallbackQueryHandler with ConversationHandler"
        "\nhttps://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/inlinekeyboard2.py",
        "/conversationbot to try simple ConversationHandler"
        "\nhttps://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/conversationbot.py",
        "/conversationbot2 to try complex ConversationHandler with ConversationHandler"
        "\nhttps://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/conversationbot2.py",
        "/set <seconds> to set a timer"
        "/unset to unset any timer"
        "\nhttps://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/timerbot.py",
        "Thanks",
    ]
    update.message.reply_text("\n\n".join(msg), disable_web_page_preview=True)


START_HANDLERS = [CommandHandler("start", start)]
