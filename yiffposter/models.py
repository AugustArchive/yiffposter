"""
Yiff Autoposter for Telegram

Copyright (c) August 2020-present

File: models.py

Description: List of models available for type-safety with Python, this has the
[APIRepo] model class, which is a model-class for yiffposter/apis
"""

class APIRepo:
  """ Model class for APIs, must override a "on_request" call """

  def __init__(self, bot, api: str, has_sources: bool=False):
    """
      Creates a new [APIRepo] instance

      Params:
        self: APIRepo - This class instance
        bot: Bot -
        api: str - API name to show
        has_sources: bool = False -
    """

    self.sources = has_sources
    self.api = api
    self.bot = bot

  def on_request(self):
    """ Creates a request, this must be overrided """
    raise Exception(f"API Repository for {self.api}#on_request must be implemented")
