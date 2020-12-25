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

const Replacement1 = new RegExp('([_*\[\]()~`>\#\+\-=|\.!])');
const Replacement2 = new RegExp('\\\\([_*\[\]()~`>\#\+\-=|\.!])');

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
    text = text
      .replace(Replacement1, '\\$1')
      .replace(Replacement2, '$1');

    this.logger.request(`-> https://api.telegram.org/bot${this.token}/sendMessage?chat_id=${chatID}&parse_mode=MarkdownV2&text=${text}`);
    return this.client.request({
      method: 'POST',
      url: `/sendMessage?chat_id=${chatID}&parse_mode=Markdown&text=${encodeURIComponent(text.replaceAll('.', '\\.'))}`
    }).then(res => {
      const data = res.json();
      this.logger.request(`<- ${JSON.stringify(data, null, 2)}`);
    });
  }

  sendPhoto(chatID: string, url: string, caption: string) {
    caption = caption
      .replace(Replacement1, '\\$1')
      .replace(Replacement2, '$1');

    console.log(caption);

    this.logger.info(`-> /sendPhoto?chat_id=${chatID}&parse_mode=MarkdownV2`, {
      caption: encodeURIComponent(caption),
      photo: encodeURIComponent(url)
    });

    return this.client.request({
      method: 'POST',
      url: `/sendPhoto?chat_id=${chatID}&parse_mode=MarkdownV2`,
      data: { caption: encodeURIComponent(caption).replace('.', '\\\\.'), photo: encodeURIComponent(url).replace('.', '\\\\.') }
    }).then(res => {
      const data = res.json();
      this.logger.request(`<- ${JSON.stringify(data, null, 2)}`);
    });
  }
}
