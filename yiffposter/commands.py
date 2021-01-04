"""
Yiff Autoposter for Telegram

Copyright (c) August 2020-present

File: commands.py

Description: List of commands that is ran when you enter the bot's DMs
"""

from telegram.ext import CallbackContext
from telegram import Update

import random

# OwOifying

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def last_replace(s, old, new):
  li = s.rsplit(old, 1)
  return new.join(li)

def make_owo(text):
  smileys = [';;w;;', '^w^', '>w<', 'UwU', '(・`ω\´・)', '(´・ω・\`)']

  text = text.replace('L', 'W').replace('l', 'w')
  text = text.replace('R', 'W').replace('r', 'w')

  text = last_replace(text, '!', '! {}'.format(random.choice(smileys)))
  text = last_replace(text, '?', '? owo')
  text = last_replace(text, '.', '. {}'.format(random.choice(smileys)))

  for v in vowels:
    if 'n{}'.format(v) in text:
      text = text.replace('n{}'.format(v), 'ny{}'.format(v))
      if 'N{}'.format(v) in text:
        text = text.replace('N{}'.format(v), 'N{}{}'.format('Y' if v.isupper() else 'y', v))
  return text
  
# Commands

def start(update: Update, ctx: CallbackContext):
  update.message.reply_text("""
  henlo, I am an autoposter bot that posts yiff every 30 minutes!
  -=- Managed by @auguwu -=-

  If you want your group to be listed, contact Chris (@auguwu) to get your list added.
""")

def owoify(update: Update, ctx: CallbackContext):
  try: 
    update.message.reply_text(make_owo(message.text))
  except Exception as e:
    update.message.reply_text(f"Calc your code sucks heres the error: `{e}`")
