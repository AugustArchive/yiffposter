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

  def _run_yiff(self, tries: int=0):
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
        print(f'[yiffposter:report] Unable to post to chat ID {idx}, view trace below')
        print(e)

        if tries != TRIES:
          tries += 1
          print(f'[yiffposter:report] Reporting to {idx} again... ({tries}/{TRIES})')
          self._run_yiff(tries)
        else:
          print(f'[yiffposter:report] Reached maximum amount of tries to post, sending failed message... (tries={TRIES})')
          self.bot.telegram.send_message(idx, "Unable to post due to a parsing error, check console for more details.")
