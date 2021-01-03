"""
Yiff Autoposter for Telegram

Copyright (c) August 2020-present

File: cron.py

Description: Cron scheduler to post every hour
"""

from .config import IDS
from telegram import ParseMode

import schedule
import logging
import time

class Scheduler:
  def __init__(self, bot):
    self.logger = logging.getLogger(__name__)
    self.bot = bot

  def end(self):
    schedule.clear()

  def start(self):
    self.run_yiff()
    schedule.every(30).minutes.do(self.run_yiff)

    #while True:
    #  try:
    #    schedule.run_pending()
    #    time.sleep(1)
    #  except KeyboardInterrupt:
    #    self.end()
    #  except Exception as e:
    #    self.logger.info(msg="Received an exception while running scheduler", exc_info=e)
    
  def run_yiff(self):
    for idx in IDS:
      data = self.bot.requests.request()
      caption = f"[ Host {data['host']} ]\nURL: {data['url']}"

      if data['artists'] != None and len(data['sources']) > 0:
        artists = ", ".join(data['artists'])
        caption += f"\nArtists: {artists}"

      if data['sources'] != None and len(data['sources']) > 0:
        i = 0
        caption += "\nSource: "

        for source in data['sources']:
          i += 1
          is_end = i == len(data['sources'])
          prefix = "| " if not is_end else ""

          caption += f"[Source #{i}]({source}) {prefix}"

      self.bot.bot.send_photo(chat_id=idx, photo=data['url'], caption=caption, parse_mode=ParseMode.MARKDOWN_V2)
