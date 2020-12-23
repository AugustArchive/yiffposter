"""
Yiff Autoposter for Telegram
Copyright (c) August 2020-present

File: telegram.py
Description: Minimal REST API to interact with Telegram
"""

from .config import TOKEN

import asyncio
import aiohttp
import typing

class TelegramAPI:
  """ Represents a minimal REST API for Telegram's bot API """

  def __init__(self):
    """
      Creates a new instance of [TelegramAPI]

      Params:
        self: TelegramAPI - The class instance
    """

    self.http = aiohttp.ClientSession(loop=asyncio.get_event_loop())

  async def request(self, method: str, endpoint: str, **kwargs) -> dict:
    """
      Private function to create requests to Telegram

      Params:
        self: TelegramAPI - The class instance
        method: str - The HTTP method verb to use
        endpoint: str - The endpoint to use, example: `getMe`
        data: ? - The data to send to Telegram (only used in `POST` http method verb)

      Returns: 
        dict[?] - JSON response from Telegram
    """

    data = kwargs.get('data', None)
    async with self.http as session:
      if method == "get":
        if data != None:
          raise Exception("Can't pass data in with a GET request")

        async with session.get(f"https://api.telegram.org/bot{TOKEN}{endpoint}") as resp:
          d = await resp.json()

          print(f"[yiffposter:telegram] Received {resp.status} from {endpoint}")
          return d
      elif method == "post":
        headers = {}

        if data:
          headers["content-type"] = "application/json"

        async with session.post(f"https://api.telegram.org/bot{TOKEN}{endpoint}", headers=headers, json=data) as resp:
          json = await resp.json()

          print(f"[yiffposter:telegram] Received {resp.status} from {endpoint}")
          return json
      else:
        raise Exception(f"HTTP Method verb was not get/post, received {method}")

  async def get_self(self) -> dict:
    """
      Get's the bot's information
      
      Params:
        self: TelegramAPI - The class instance

      Returns: 
        dict[?] - JSON response from Telegram
    """
    return await self.request("get", "/getMe")

  async def send_message(self, chat_id: str, text: str, **kwargs) -> dict:
    """
      Sends a message to the specified [chat_id]

      Params:
        self: TelegramAPI - The class instance
        chat_id: str - The chat's ID
        text: str - The content to send
      
      Returns:
        dict[Message] - JSON response from Telegram
    """

    parse_mode = kwargs.get('parse', "MarkdownV2")
    return await self.request("post", f"/sendMessage?chat_id={chat_id}&text={text}&parse_mode={parse_mode}")

  async def send_photo(self, chat_id: str, photo_url: str, caption: typing.Union[str, None]=None) -> dict:
    """
      Sends a photo with a optional [caption] if needed

      Params:
        self: TelegramAPI - The class instance
        chat_id: str - The chat's ID
        text: str - The content to send
        caption: Union[str, None] - If we should include a caption
      
      Returns:
        dict[Message] - JSON response from Telegram
    """

    url = f"/sendPhoto?chat_id={chat_id}&photo={photo_url}"
    if caption is not None:
      caption = caption.replace(" ", "%20")
      url += f"&caption={caption}"

    return await self.request("post", url)
