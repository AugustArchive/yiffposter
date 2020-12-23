"""
Yiff Autoposter for Telegram
Copyright (c) August 2020-present

File: run.py
Description: Runs the bot
"""

from yiffposter.bot import Bot
import sys

bot = Bot()

if __name__ == '__main__':
  print("[yiffposter:runner] Running bot...")

  try:
    bot.run()
  except KeyboardInterrupt:
    print("[yiffposter:runner] Recevied CTRL+C signal")
    sys.exit(1)
