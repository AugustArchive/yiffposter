/**
 * Yiff Autoposter for Telegram
 *
 * Copyright (c) August 2020-present
 */

import { Repository, RequestData } from '../repository';

export class FurryBotAPI extends Repository {
  constructor() {
    super('api.furry.bot', '@Donovan_DMC');
  }

  request() {
    const headers = {};
    if (process.env.FURRY_BOT !== undefined)
      headers['Authorization'] = process.env.FURRY_BOT;

    return this.bot.http.request({
      method: 'get',
      url: 'https://api.furry.bot/V2/furry/yiff/gay',
      headers
    }).then(res => {
      const data = res.json();
      return {
        artists: data.images[0].artists,
        sources: data.images[0].sources,
        url: data.images[0].url
      } as RequestData;
    });
  }
}
