from .august import AugustAPI
from .furrybot import FurryBotAPI
from .roman import RomanAPI

import random

class RequestHandler:
  def __init__(self, bot):
    self.apis = {
      "floofy": AugustAPI(bot),
      "awoooo": RomanAPI(bot),
      "furry": FurryBotAPI(bot)
    }

  def request(self):
    key = random.choice(list(self.apis.keys()))
    api = self.apis[key]

    return api.request()
