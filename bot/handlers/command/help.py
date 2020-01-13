from telegram.ext import CommandHandler


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


HELP_HANDLERS = [
    CommandHandler('help', help)
]
