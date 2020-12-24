"""
Yiff Autoposter for Telegram

Copyright (c) August 2020-present

File: cron.py

Description: Cron scheduler to post every hour
"""

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

  def _run_yiff(self):
    data = self.bot.requester.request()
    caption = f"API: {data['host']}"

    if data['artists'] != None:
      artists = ", ".join(data['artists'])
      caption += f"\nArtist(s): {artists}"
    else:
      caption += f"\nArtist: API doesn't cover this"

    if data['sources'] != None:
      i = 0
      caption += "\nSource: "

      for source in data['sources']:
        i += 1
        caption += f"[Source {i}]({source}) | "
    else:
      caption += f"\nSources: API doesn't cover this"
      
    caption += f"\nURL: {data['url']}"

    # TODO: send to all chats
    self.bot.telegram.send_photo("-1001431058138", data['url'], caption)
