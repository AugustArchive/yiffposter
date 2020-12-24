"""
Yiff Autoposter for Telegram

Copyright (c) August 2020-present

File: utils.py

Description: Here are some useful functions used throughout the project
"""

import re

def escape_md(string: str) -> str:
  parse = re.sub(r"([_*\[\]()~`>\#\+\-=|\.!])", r"\\\1", string)
  return re.sub(r"\\\\([_*\[\]()~`>\#\+\-=|\.!])", r"\1", parse) # don't hate me for this pls, also stolen code bacause fuck regex
  