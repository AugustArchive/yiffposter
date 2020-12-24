"""
Yiff Autoposter for Telegram

Copyright (c) August 2020-present

File: apis/requester.py

Description: Utility class to fetch from different APIs
"""

from .furrybot import FurryBotAPI
from .august import AugustAPI
from .roman import RomanAPI

import random

class Requester:
  def __init__(self, bot):
    self.apis = {}
    self.bot = bot

    self.register()

  def register(self):
    self.apis["furry"] = FurryBotAPI(self.bot)
    self.apis["floof"] = AugustAPI(self.bot)
    self.apis["roman"] = RomanAPI(self.bot)

  def request(self):
    key = random.choice(list(self.apis.keys()))
    api = self.apis[key]

    return api.on_request()
