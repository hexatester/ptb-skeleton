import os
from .base import BaseBot
from bot.config import WebhookConfig


class WebhookBot(BaseBot):
    def __init__(self, config: WebhookConfig, *args, **kwargs):
        self._config = config
        super(WebhookBot, self).__init__(token=config.token,
                                         flood_limit=config.flood_limit, presistence=config.presistence)

    def start(self):
        if self._config.heroku:
            return self.heroku()
        return self.default()

    def register(self, funct):
        funct(self.Updater.dispatcher)

    def heroku(self):
        self.Updater.start_webhook(
            listen='0.0.0.0',
            port=os.getenv('PORT', 8443),
            url_path=self._config.token,
            clean=self._config.clean
        )
        self.Updater.bot.set_webhook(
            self._config.url_path + self._config.token)
        self.Updater.idle()

    def default(self):
        self.Updater.start_webhook(
            listen=self._config.listen,
            port=self._config.port,
            url_path=self._config.url_path,
            cert=self._config.cert,
            key=self._config.key,
            clean=self._config.clean,
            webhook_url=self._config.webhook_url
        )
