"""
Yiff Autoposter for Telegram
Copyright (c) August 2020-present

File: run.py
Description: Runs the bot
"""

from yiffposter.bot import Bot

import logging
import sys

logging.basicConfig(format="[%(asctime)s] [%(name)s | %(levelname)s] ~> %(message)s", level=logging.INFO)

logger = logging.getLogger("yiffposter.runner")
bot = Bot()

if __name__ == '__main__':
  try:
    bot.run()
  except KeyboardInterrupt:
    sys.exit(1)
  except e:
    logger.error('Unknown exception has occured')
    print(e)

    sys.exit(1)
