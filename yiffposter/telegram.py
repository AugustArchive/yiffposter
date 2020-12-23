"""
Yiff Autoposter for Telegram
Copyright (c) August 2020-present

File: telegram.py
Description: Minimal REST API to interact with Telegram
"""

from .config import TOKEN
import asyncio
import aiohttp

class TelegramAPI:
  """ Represents a minimal REST API for Telegram's bot API """

  def __init__(self):
    """
      Creates a new instance of [TelegramAPI]

      Params:
        self: TelegramAPI - The class instance
    """

    self.http = aiohttp.ClientSession(loop=asyncio.get_event_loop())

  async def get_self(self) -> dict:
    """
      Get's the bot's information
      
      Params:
        self: TelegramAPI - The class instance

      Returns: 
        dict[?] - JSON response from Telegram
    """
    async with self.http as session:
      async with session.get(f"https://api.telegram.org/bot{TOKEN}/getMe") as resp:
        print(resp.status)
        print(await resp.json())
