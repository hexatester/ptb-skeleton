from .callback import register_callbacks
from .command import register_commands
from .conversation import register_conversations
from .error import register_errors

REGISTERS = [
    register_errors,
    register_conversations,
    register_callbacks,
    register_commands
]


def register(dispatcher):
    if REGISTERS:
        for register in REGISTERS:
            register(dispatcher)
