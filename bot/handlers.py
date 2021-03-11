from telegram.ext import Dispatcher

from bot.callback import register_callbacks
from bot.command import register_commands
from bot.conversation import register_conversations
from bot.error import register_errors

REGISTERS = [
    register_errors,
    register_conversations,
    register_callbacks,
    register_commands,
]


def register(dispatcher: Dispatcher):
    if REGISTERS:
        for register in REGISTERS:
            register(dispatcher)
