"""
Yiff Autoposter for Telegram

Copyright (c) August 2020-present

File: cron.py

Description: Cron scheduler to post every hour
"""

from .config import IDS, TRIES
from .utils import escape_md

import schedule

class CronScheduler:
  """ Class to run schedulers using the [schedule] package """

  def __init__(self, bot):
    """
      Creates a new instance of [CronScheduler]

      Params:
        self: CronScheduler - This class instance
        bot: Bot - The bot that is running
    """

    self.bot = bot

  def init(self):
    self._run_yiff()
    schedule.every(30).minutes.do(self._run_yiff)

  def _post(self, idx: str, url: str, caption: str) -> dict:
    return self.bot.telegram.send_photo(idx, url, caption)

  def _run_yiff(self):
    for idx in IDS:
      try:
        data = self.bot.requester.request()
        caption = f"API: {escape_md(data['host'])}"

        if data['artists'] != None:
          artists = ", ".join(data['artists'])
          caption += escape_md(f"\nArtists: {artists}")

        if data['sources'] != None:
          i = 0
          caption += "\nSource: "

          for source in data['sources']:
            i += 1
            is_end = i == len(data['sources'])
            prefix = "\\| " if not is_end else ""

            caption += f"[Source #{i}]({escape_md(source)}) {prefix}"

        if data['owner'] != None:
          owner = data['owner'].replace("_", "\\_")
          caption += f"\nAPI Owner: {owner}"
          
        caption += f"\nURL: {escape_md(data['url'])}"
        self._post(idx, data['url'], caption)
      except Exception as e:
        print(e)
        self.bot.telegram.send_message(idx, "Unable to post due to a parsing error, trying after another 30 minutes")
