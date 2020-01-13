from bot.config import CONFIG, WebhookConfig, PollingConfig
from bot.logging import logging
from bot.bots import PollingBot, WebhookBot
from bot.handlers import register


def start():
    if isinstance(CONFIG, WebhookConfig):
        Bot = WebhookBot(CONFIG)
    elif isinstance(CONFIG, PollingConfig):
        Bot = PollingBot(CONFIG)
    Bot.register(register)
    Bot.start()
