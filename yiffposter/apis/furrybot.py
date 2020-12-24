"""
Yiff Autoposter for Telegram

Copyright (c) August 2020-present

File: apis/furrybot.py

Description: REST API for https://api.furry.bot, created by Donovan_DMC
"""

from yiffposter.models import APIRepo
from yiffposter.config import FURRY_BOI
import requests

class FurryBotAPI(APIRepo):
  def __init__(self, bot):
    super().__init__(bot, "api.furry.bot", False)

  def on_request(self):
    res = requests.get("https://api.furry.bot/V2/furry/yiff/gay", headers={"Authorization": FURRY_BOI})
    res.raise_for_status()

    print(f"[yiffposters:api:furry] Received {res.status_code} on https://api.furry.bot/V2/furry/yiff/gay")
    
    data = res.json()
    image = data['images'][0]

    return {
      "url": image['url'],
      "sources": image['sources'],
      "host": self.api,
      "artists": image['artists']
    }
