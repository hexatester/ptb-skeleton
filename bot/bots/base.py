#!/usr/bin/env python3
# encoding=utf-8

'''
MessageQueue usage example with @queuedmessage decorator.
Provide your bot token with `TOKEN` environment variable or list it in
file `token.txt`
'''
import telegram.bot
from telegram.ext import Updater
from telegram.ext import messagequeue as mq


class MQBot(telegram.bot.Bot):
    '''A subclass of Bot which delegates send method handling to MQ'''

    def __init__(self, *args, is_queued_def=True, mqueue=None, **kwargs):
        super(MQBot, self).__init__(*args, **kwargs)
        # below 2 attributes should be provided for decorator usage
        self._is_messages_queued_default = is_queued_def
        self._msg_queue = mqueue or mq.MessageQueue()

    def __del__(self):
        try:
            self._msg_queue.stop()
        except:
            pass

    @mq.queuedmessage
    def send_message(self, *args, **kwargs):
        '''Wrapped method would accept new `queued` and `isgroup`
        OPTIONAL arguments'''
        return super(MQBot, self).send_message(*args, **kwargs)


def get_flood_limit_updater(token: str, persistence=None):
    import telegram
    from telegram.utils.request import Request
    q = mq.MessageQueue(all_burst_limit=3, all_time_limit_ms=3000)
    # set connection pool size for bot
    request = Request(con_pool_size=8)
    testbot = MQBot(token, request=request, mqueue=q)
    return Updater(bot=testbot, persistence=persistence, use_context=True)


def get_updater(token: str, flood_limit=False, persistence=None):
    return Updater(token, persistence=persistence, use_context=True)


class BaseBot:
    def __init__(self, token: str, flood_limit=False, persistence=None, clean=True):
        if flood_limit:
            self.Updater: Updater = get_flood_limit_updater(
                token, persistence=persistence)
        else:
            self.Updater: Updater = get_updater(
                token, persistence=persistence)
