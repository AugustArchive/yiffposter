"""
Yiff Autoposter for Telegram

Copyright (c) August 2020-present

File: bot.py

Description: The bot's source code, which runs the bot and creates
a cron scheduler to post yiff every hour (i.e: 06:00) from sorts of APIs.

You can make a PR and add it in yiffposter/api, it must extend the [APIRepo]
class under yiffposter/models.py, all responses can be in any encoding,
you must override [APIRepo.get_image] to actually get the response, it'll
sliently fail if it reaches a non-200 status code.

Example:

```py
from yiffposter.models import APIRepo

class MyAPI(APIRepo):
  def __init__(self, bot):
    super(self, APIRepo).__init__(bot, "<url to get info>")

  async def get_image(self) -> str:
    # get image here, must return a string
```
"""

from .telegram import TelegramAPI
from .events import EventBus
from .cron import CronScheduler
#from .apis import APIRequester

import schedule
import time
import sys

class Bot:
  def __init__(self):
    #self.requester = APIRequester()
    self.telegram = TelegramAPI()
    #self.events = EventBus(bot=self)
    self.cron = CronScheduler(bot=self)

  def run(self):
    print("[yiffposter:bot] Post setting up...")

    #self.events.init()
    self.cron.init()

    while True:
      try:
        #self.events.handle_updates()
        schedule.run_pending()
        time.sleep(3)
      except KeyboardInterrupt:
        print('[yiffposter:bot] Killing event bus and cron scheduler...')

        schedule.clear()
        sys.exit(1)
