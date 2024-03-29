import sys

from telegram.ext import Updater
from bot.config import BOT_TOKEN, PORT, APP_URL
from bot.handlers import register


def main():
    updater = Updater(BOT_TOKEN)
    register(updater.dispatcher)
    if PORT:
        updater.start_webhook(
            listen="0.0.0.0",
            port=PORT,
            url_path=BOT_TOKEN,
            webhook_url=APP_URL + BOT_TOKEN,
        )
    else:
        updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    sys.exit(main())
