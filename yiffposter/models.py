"""
Yiff Autoposter for Telegram

Copyright (c) August 2020-present

File: models.py

Description: List of models available for type-safety with Python, this has the
[APIRepo] model class, which is a model-class for yiffposter/apis
"""

class APIRepo:
  def __init__(self, bot, api: str):
    self.api = api
    self.bot = bot

  def request(self):
    raise Exception(f"API Repository for {self.api}#on_request must be implemented")
