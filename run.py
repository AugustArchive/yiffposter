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
  bot.run()
