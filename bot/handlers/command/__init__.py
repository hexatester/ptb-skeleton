from .alarm import ALARM_HANDLERS
from .cancel import CANCEL_HANDLERS
from .deeplinking import DEEPLINKING_HANDLERS
from .help import HELP_HANDLERS
from .start import START_HANDLERS


HANDLERS = []
HANDLERS.extend(ALARM_HANDLERS)
HANDLERS.extend(DEEPLINKING_HANDLERS)
HANDLERS.extend(HELP_HANDLERS)
HANDLERS.extend(START_HANDLERS)
# Always register cancel at the end
HANDLERS.extend(CANCEL_HANDLERS)


def register_commands(dispatcher):
    if HANDLERS:
        for handler in HANDLERS:
            dispatcher.add_handler(handler)
