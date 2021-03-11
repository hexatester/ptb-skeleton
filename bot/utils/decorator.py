import logging
from functools import wraps
from telegram import ParseMode, Update
from telegram.ext import CallbackContext

# Require x non-command messages between each /rules etc.
RATE_LIMIT_SPACING = 2


def rate_limit_tracker(update: Update, context: CallbackContext):
    data = context.chat_data.get("rate_limit", {})

    for key in data.keys():
        data[key] += 1


def rate_limit(f):
    """
    Rate limit command so that RATE_LIMIT_SPACING non-command messages are
    required between invocations.
    """

    @wraps(f)
    def wrapper(update, context, *args, **kwargs):
        # Get rate limit data
        try:
            data = context.chat_data["rate_limit"]
        except KeyError:
            data = context.chat_data["rate_limit"] = {}

        # If we have not seen two non-command messages since last of type `f`
        if data.get(f, RATE_LIMIT_SPACING) < RATE_LIMIT_SPACING:
            logging.debug("Ignoring due to rate limit!")
            return

        data[f] = 0

        return f(update, context, *args, **kwargs)

    return wrapper
