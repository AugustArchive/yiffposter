"""
Yiff Autoposter for Telegram

Copyright (c) August 2020-present

File: apis/roman.py

Description: REST API for https://api.awooo.space, created by Roman
"""

from yiffposter.models import APIRepo

import logging
import requests

class RomanAPI(APIRepo):
  def __init__(self, bot):
    super().__init__(bot, "api.awooo.space")

    self.logger = logging.getLogger(__name__)

  def request(self):
    res = requests.get("https://api.awooo.space/yiff", headers={
      "User-Agent": "auguwu/yiffposter (v0.0.0)"
    })

    res.raise_for_status()

    self.logger.info(f"Received {res.status_code} on https://api.awooo.space/yiff")
    
    data = res.json()
    return {
      "url": data['url'],
      "sources": None,
      "host": self.api,
      "artists": None,
      "owner": "@oko_123"
    }
