#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/timerbot.py
Simple Bot to send timed Telegram messages.
This Bot uses the Updater class to handle the bot and the JobQueue to send
timed messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Alarm Bot example, sends a message after a set time.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
import logging
from telegram.ext import CommandHandler


logger = logging.getLogger(__name__)


def alarm(context):
    """Send the alarm message."""
    job = context.job
    context.bot.send_message(job.context, text="Beep!")


def set_timer(update, context):
    """Add a job to the queue."""
    chat_id = update.message.chat_id
    try:
        # args[0] should contain the time for the timer in seconds
        due = int(context.args[0])
        if due < 0:
            update.message.reply_text("Sorry we can not go back to future!")
            return
        # Add job to queue and stop current one if there is a timer already
        if "job" in context.chat_data:
            old_job = context.chat_data["job"]
            old_job.schedule_removal()
        new_job = context.job_queue.run_once(alarm, due, context=chat_id)
        logger.info("alarm %s secons for chat_id : %s", due, chat_id)
        context.chat_data["job"] = new_job
        update.message.reply_text("Timer successfully set!")
    except (IndexError, ValueError):
        update.message.reply_text("Usage: /set <seconds>")


def unset(update, context):
    """Remove the job if the user changed their mind."""
    if "job" not in context.chat_data:
        update.message.reply_text("You have no active timer")
        return
    job = context.chat_data["job"]
    job.schedule_removal()
    del context.chat_data["job"]
    update.message.reply_text("Timer successfully unset!")


ALARM_HANDLERS = [
    CommandHandler(
        "set", set_timer, pass_args=True, pass_job_queue=True, pass_chat_data=True
    ),
    CommandHandler("unset", unset, pass_chat_data=True),
]
