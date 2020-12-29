/**
 * Yiff Autoposter for Telegram
 *
 * Copyright (c) August 2020-present
 *
 * File: src/requests.ts
 * Description: Class to handle API requests to Telegram
 */

import { HttpClient } from '@augu/orchid';
import Logger from './logger';
import { replaceMD } from './utils';

const re: RegExp = /(%5C)/g;

export default class TelegramAPI {
  private logger: Logger;
  private client: HttpClient;

  constructor(private token: string) {
    this.logger = new Logger('requests');
    this.client = new HttpClient({
      defaults: {
        baseUrl: `https://api.telegram.org/bot${token}`
      }
    });
  }

  sendMessage(chatID: string, text: string) {
    text = encodeURIComponent(replaceMD(text) as string).replace(re, '\\');

    this.logger.request(`-> https://api.telegram.org/bot${this.token}/sendMessage?chat_id=${chatID}&parse_mode=MarkdownV2&text=${text}`);
    return this.client.request({
      method: 'POST',
      url: `/sendMessage?chat_id=${chatID}&parse_mode=Markdown&text=${text}`
    }).then(res => {
      const data = res.json();
      this.logger.request(`<- ${JSON.stringify(data, null, 2)}`);
    });
  }

  sendPhoto(chatID: string, url: string, caption: string) {
    caption = encodeURIComponent(replaceMD(caption) as string).replace(re, '\\');
    url = encodeURIComponent(replaceMD(url) as string).replace(re, '\\');

    this.logger.info(`-> /sendPhoto?chat_id=${chatID}&parse_mode=MarkdownV2`, {
      caption: caption,
      photo: url
    });

    return this.client.request({
      method: 'POST',
      url: `/sendPhoto?chat_id=${chatID}&parse_mode=MarkdownV2`,
      data: { caption:caption, photo: url }
    }).then(res => {
      const data = res.json();
      this.logger.request(`<- ${JSON.stringify(data, null, 2)}`);
    });
  }
}
