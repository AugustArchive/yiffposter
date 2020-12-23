"""
Yiff Autoposter for Telegram
Copyright (c) August 2020-present

File: run.py
Description: Runs the bot
"""

from yiffposter.bot import Bot
import asyncio
import sys

loop = asyncio.get_event_loop()
bot = Bot()

async def main():
  print("[yiffposter] Running bot...")

  try:
    await bot.run()
  except KeyboardInterrupt:
    print("[yiffposter] Gotten CTRL+C signal")

    await bot.telegram.http.close()
    sys.exit(0)

loop.run_until_complete(main())
