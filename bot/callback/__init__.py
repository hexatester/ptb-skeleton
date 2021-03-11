from .inlinekeyboard import INLINEKEYBOARD_HANDLERS
from .inlinekeyboard2 import INLINEKEYBOARD2_HANDLERS


HANDLERS = []
HANDLERS.extend(INLINEKEYBOARD_HANDLERS)
HANDLERS.extend(INLINEKEYBOARD2_HANDLERS)


def register_callbacks(dispatcher):
    if HANDLERS:
        for handler in HANDLERS:
            dispatcher.add_handler(handler)
