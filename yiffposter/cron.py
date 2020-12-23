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

