from .conversationbot import CONVERSATIONBOT_HANDLERS
from .conversationbot2 import CONVERSATIONBOT2_HANDLERS


HANDLERS = []
HANDLERS.extend(CONVERSATIONBOT_HANDLERS)
HANDLERS.extend(CONVERSATIONBOT2_HANDLERS)


def register_conversations(dispatcher):
    if HANDLERS:
        for handler in HANDLERS:
            dispatcher.add_handler(handler)
