"""
Copyright (c) August 2020-present

telegram.py - Minimal REST API to interact with Telegram
"""

from .config import TOKEN

import requests
import typing

class TelegramAPI:
  """ Represents a minimal REST API for Telegram's bot API """

  def request(self, method: str, endpoint: str, **kwargs) -> dict:
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
    if method == "get" or method == "GET":
      if data != None:
        raise Exception("Can't pass data in with a GET request")

      res = requests.get(f"https://api.telegram.org/bot{TOKEN}{endpoint}")
      res.raise_for_status()

      print(f"[yiffposter:telegram] Received {res.status_code} on {endpoint}")
      return res.json()
    elif method == "post" or method == "POST":
      headers = {}

      if data:
        headers["content-type"] = "application/json"

      res = requests.post(f"https://api.telegram.org/bot{TOKEN}{endpoint}", json=data)
      res.raise_for_status()

      print(f"[yiffposter:telegram] Received {res.status_code} on {endpoint}")
      return res.json()
    else:
      raise Exception("Invalid HTTP method verb, only GET and POST is supported")

  def get_self(self) -> dict:
    """
      Get's the bot's information
      
      Params:
        self: TelegramAPI - The class instance

      Returns: 
        dict[?] - JSON response from Telegram
    """
    return self.request("get", "/getMe")

  def send_message(self, chat_id: str, text: str, **kwargs) -> dict:
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
    return self.request("post", f"/sendMessage?chat_id={chat_id}&text={text}&parse_mode={parse_mode}")

  def send_photo(self, chat_id: str, photo_url: str, caption: typing.Union[str, None]=None) -> dict:
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

    url = f"/sendPhoto?chat_id={chat_id}&photo={photo_url}&parse_mode=Markdown"
    if caption is not None:
      caption = caption.replace(" ", "%20")
      url += f"&caption={caption}"

    return self.request("post", url)
