"""
Yiff Autoposter for Telegram

Copyright (c) August 2020-present

File: apis/august.py

Description: REST API for https://api.floofy.dev, created by August
"""

from yiffposter.models import APIRepo
import requests

class AugustAPI(APIRepo):
  def __init__(self, bot):
    super().__init__(bot, "api.floofy.dev", False)

  def on_request(self):
    res = requests.get("https://api.floofy.dev/yiff")
    res.raise_for_status()

    print(f"[yiffposters:api:august] Received {res.status_code} on https://api.floofy.dev/yiff")
    
    data = res.json()
    return {
      "url": data['url'],
      "sources": None,
      "host": self.api,
      "artists": None
    }
