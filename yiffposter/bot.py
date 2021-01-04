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

from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Bot as TBot, ParseMode
from urllib.parse import urlparse
from .requests import RequestHandler
from .commands import start, owoify, help as halp
from .config import TOKEN, IDS
from sys import exit

import logging
import re

def escape_md(string: str) -> str:
  parse = re.sub(r"([_*\[\]()~`>\#\+\-=|\.!])", r"\\\1", string)
  return re.sub(r"\\\\([_*\[\]()~`>\#\+\-=|\.!])", r"\1", parse) # don't hate me for this pls, also stolen code bacause fuck regex

logging.basicConfig(format="[%(asctime)s] [%(name)s | %(levelname)s] ~> %(message)s", level=logging.INFO)

class Bot:
  def __init__(self):
    self.requests = RequestHandler(bot=self)
    self.updater = Updater(TOKEN, use_context=True, user_sig_handler=self._on_signal)
    self.logger = logging.getLogger(__name__)
    self.bot = TBot(TOKEN)

  def _on_signal(self, signum, frame):
    self.logger.warn("Process has ended")
    exit(1)

  def _on_error(self, update, ctx):
    self.logger.error(msg="Exception has occured while getting updates", exc_info=ctx.error)

  def run(self):
    dispatcher = self.updater.dispatcher

    self.logger.info("Starting bot instance...")
    dispatcher.add_handler(CommandHandler("help", halp))
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("image", self.command_image))
    dispatcher.add_handler(CommandHandler("owoify", owoify))
    dispatcher.add_error_handler(self._on_error)

    self._queue()
    self.updater.start_polling()
    self.updater.idle()

    self.logger.info("Bot is now started! <3")

  def command_image(self, update, context):
    try:
      api = context.args[0]
      if api == "list":
        apis = ", ".join(self.requests.apis.keys())
        update.message.reply_text(apis)
        return

      if api not in self.requests.apis.keys():
        update.message.reply_text(f"API {api} was not found.")
        return

      data = self._get_content(self.requests.apis[api])
      update.message.reply_photo(photo=data['data']['url'], caption=data['caption'], parse_mode=ParseMode.MARKDOWN_V2)
    except (IndexError, ValueError):
      data = self._get_content(None)
      update.message.reply_photo(photo=data['data']['url'], caption=data['caption'], parse_mode=ParseMode.MARKDOWN_V2)

  def _queue(self):
    dispatcher = self.updater.dispatcher
    
    for idx in IDS:
      self.logger.debug(f"Building job for chat ID {idx}...")
      r = self._get_content()
      self.bot.send_photo(chat_id=idx, photo=r['data']['url'], caption=r['caption'], parse_mode=ParseMode.MARKDOWN_V2)

      dispatcher.job_queue.run_repeating(self._run_yiff, 1800, name=f"yiffposter:chat:{idx}")

  def _get_content(self, requester=None):
    data = requester.request() if requester is not None else self.requests.request()
    caption = escape_md(f"[ {data['host']} by {data['owner']} ]\n\nURL: {data['url']}")

    if data['artists'] != None and len(data['sources']) > 0:
      artists = ", ".join(data['artists'])
      caption += escape_md(f"\nArtists: {artists}")

    if data['sources'] != None and len(data['sources']) > 0:
      i = 0
      caption += escape_md("\n\nSource(s):")

      for source in data['sources']:
        i += 1
        caption += escape_md(f"\n- #{i}: {source}")

    return {
      "data": data,
      "caption": caption
    }

  def _run_yiff(self, context: CallbackContext):
    for idx in IDS:
      data = self._get_content()
      context.bot.send_photo(chat_id=idx, photo=data['data']['url'], caption=data['caption'], parse_mode=ParseMode.MARKDOWN_V2)
