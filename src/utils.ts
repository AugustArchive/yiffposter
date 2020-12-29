/**
 * Yiff Autoposter for Telegram
 *
 * Copyright (c) August 2020-present
 *
 * File: src/utils.ts
 * Description: A file with commonly used stuff throughout the project, blah blah blah...
 */

export const replaceMD = (text: string | string[]): string | string[] => {
  const replacepls = (_text: string): string => {
    const re1 = /([_*\[\]()~`>\#\+\-=|\.!])/g;
    const re2 = /\\\\([_*\[\]()~`>\#\+\-=|\.!])/g;

    if (re1.test(_text)) {
      const parse = _text.replace(re1, '\\$1');
      _text = parse.replace(re2, '$1');
    }
    return _text;
  };

  if (typeof text === 'string') {
    text = replacepls(text);
  } else {
    const last = text.length - 1;
    for (let i = 0; i < text.length; i++) {
      text[i] = replacepls(text[i]);
      if (i === last) break;
    }
  }
  return text;
};

// probably inefficient as fuck, but hopefully this works. Also, sorry for my code wheeee
