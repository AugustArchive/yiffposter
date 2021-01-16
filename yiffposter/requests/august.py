"""
Yiff Autoposter for Telegram

Copyright (c) August 2020-present

File: requests/august.py

Description: REST API for https://api.floofy.dev, created by August
"""

from yiffposter.models import APIRepo

import logging
import requests

class AugustAPI(APIRepo):
  def __init__(self, bot):
    super().__init__(bot, "api.floofy.dev")

    self.logger = logging.getLogger(__name__)

  def request(self):
    res = requests.get("https://api.floofy.dev/yiff", headers={
      "User-Agent": "auguwu/yiffposter (v0.0.0)"
    })
    
    res.raise_for_status()

    self.logger.info(f"Received {res.status_code} on https://api.floofy.dev/yiff")
    
    data = res.json()
    return {
      "url": data['url'],
      "sources": data['sources'],
      "host": self.api,
      "artists": data['artists'],
      "owner": "@auguwu"
    }
