import os
import logging

logger = logging.getLogger(__name__)


class BaseConfig:
    # Place for common (same) denominator
    token = ''
    # This is global log configuration
    log_config = {
        'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        'level': logging.INFO
    }
    username = '@botfather'
    # https://github.com/python-telegram-bot/python-telegram-bot/wiki/Avoiding-flood-limits
    flood_limit = False
    # https://github.com/python-telegram-bot/python-telegram-bot/wiki/Making-your-bot-persistent
    presistence = None
    # Abandon previous update before bot starting
    clean = True


class WebhookConfig(BaseConfig):
    # Read more
    # https://github.com/python-telegram-bot/python-telegram-bot/wiki/Webhooks
    # Set your token if you using heroku as deployment method
    # https://github.com/python-telegram-bot/python-telegram-bot/wiki/Webhooks#heroku
    # https://devcenter.heroku.com/articles/config-vars
    token = os.getenv('TOKEN')
    heroku = True
    # Please fill vars bellow if heroku is False
    # https://github.com/python-telegram-bot/python-telegram-bot/wiki/Webhooks#the-integrated-webhook-server
    # https://github.com/python-telegram-bot/python-telegram-bot/wiki/Webhooks#using-nginx-with-one-domainport-for-all-bots
    # webhook_url:str = "https://<appname>.herokuapp.com/"
    webhook_url: str = None
    listen: str = None
    port: str = None
    url_path: str = None
    key: str = None
    cert: str = None


class PollingConfig(BaseConfig):
    # Set your polling/development token here
    token = ''


if os.getenv('TOKEN'):
    CONFIG = WebhookConfig()
    logger.info('You are using WebhookConfig. :)')
else:
    CONFIG = PollingConfig()
    logger.info('You are using PollingConfig. :P')
