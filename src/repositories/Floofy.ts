/**
 * Yiff Autoposter for Telegram
 *
 * Copyright (c) August 2020-present
 */

import { Repository, RequestData } from '../repository';

export class FloofyAPI extends Repository {
  constructor() {
    super('api.floofy.dev', '@auguwu');
  }

  request() {
    return this.bot.http.request({
      method: 'get',
      url: 'https://api.floofy.dev/yiff'
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
