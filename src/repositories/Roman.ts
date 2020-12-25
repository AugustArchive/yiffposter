/**
 * Yiff Autoposter for Telegram
 *
 * Copyright (c) August 2020-present
 */

import { Repository, RequestData } from '../repository';

export class RomanAPI extends Repository {
  constructor() {
    super('api.awooo.space', '@oko_123');
  }

  request() {
    return this.bot.http.request({
      method: 'get',
      url: 'https://api.awooo.space/yiff'
    }).then(res => {
      const data = res.json();
      return {
        artists: [],
        sources: [],
        url: data.url
      } as RequestData;
    });
  }
}
