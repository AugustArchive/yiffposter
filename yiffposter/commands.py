"""
Yiff Autoposter for Telegram

Copyright (c) August 2020-present

File: commands.py

Description: List of commands that is ran when you enter the bot's DMs
"""

from telegram.ext import CallbackContext
from telegram import Update

def start(update: Update, ctx: CallbackContext):
  update.message.reply_text("""
    henlo, I am an autoposter bot that posts yiff every 30 minutes!
    -=- Managed by @auguwu -=-

    If you want your group to be listed, contact Chris (@auguwu) to get your list added.
  """)
