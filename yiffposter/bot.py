"""
Yiff Autoposter for Telegram
Copyright (c) August 2020-present

File: bot.py
Description: The bot's source code, which runs the bot and creates
a cron scheduler to post yiff every hour (i.e: 06:00) from sorts of APIs.

You can make a PR and add it in yiffposter/api, it must extend the [APIRepo]
class under yiffposter/models.py, all responses can be in any encoding,
you must override [APIRepo.get_image] to actually get the response, it'll
sliently fail if it reaches a non-200 status code.

Example:

```py
from yiffposter.models import APIRepo

class MyAPI(APIRepo):
  def __init__(self, bot):
    super(self, APIRepo).__init__(bot, "<url to get info>")

  async def get_image(self) -> str:
    # get image here, must return a string
```
"""

