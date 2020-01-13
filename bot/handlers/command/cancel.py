#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.
from telegram.ext import CommandHandler


def cancel(update, context):
    """Send a message when the command /cancel is issued."""
    update.message.reply_text('Cancel what?')


CANCEL_HANDLERS = [
    CommandHandler('cancel', cancel)
]
