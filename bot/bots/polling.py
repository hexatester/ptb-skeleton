from .base import BaseBot
from bot.config import PollingConfig


class PollingBot(BaseBot):
    def __init__(self, config: PollingConfig, *args, **kwargs):
        self._config = config
        super(PollingBot, self).__init__(token=config.token,
                                         flood_limit=config.flood_limit, persistence=config.presistence)

    def start(self):
        self.Updater.start_polling(
            clean=self._config.clean
        )
        self.Updater.idle()

    def register(self, funct):
        funct(self.Updater.dispatcher)
