/**
 * Yiff Autoposter for Telegram
 *
 * Copyright (c) August 2020-present
 *
 * File: src/index.ts
 * Description: The bot's source code, which runs the bot and creates
 * a cron scheduler to post yiff every hour (i.e: 06:00) from sorts of APIs.
 */

import type { ScheduledTask } from 'node-cron';
import type { Repository } from './repository';
import * as repositories from './repositories';
import { Collection } from '@augu/immutable';
import { HttpClient } from '@augu/orchid';
import * as scheduler from './scheduler';
import { parse } from '@augu/dotenv';
import Telegram from './requests';
import { join } from 'path';
import Logger from './logger';

export class AutoYiffPoster {
  public repositories: Collection<Repository>;
  public scheduler!: ScheduledTask;
  public telegram!: Telegram;
  public logger: Logger;
  public http: HttpClient;

  constructor() {
    this.repositories = new Collection();
    this.logger = new Logger('bot');
    this.http = new HttpClient();
  }

  async start() {
    this.repositories.set('furrybot', new repositories.FurryBotAPI().init(this));
    this.repositories.set('floofy', new repositories.FloofyAPI().init(this));
    this.repositories.set('roman', new repositories.RomanAPI().init(this));

    parse({
      populate: true,
      file: join(__dirname, '..', '.env'),
      schema: {
        TELEGRAM_TOKEN: 'string',
        CHAT_IDS: 'string',
        FURRY_BOT: {
          type: 'string',
          default: undefined
        }
      }
    });

    this.telegram = new Telegram(process.env.TELEGRAM_TOKEN!);
    this.logger.info('Hello world!');

    this.scheduler = await scheduler.create(this);
  }

  async sendYiff() {
    this.logger.info('Sending yiff...');
    const repository = this.repositories.get('furrybot')!;
    const data = await repository.request();

    let caption = `URL: ${data.url}`;
    caption += `\nAPI: ${repository.api.replace(/\./g, '\\')}`;
    if (data.artists.length)
      caption += `\nArtist(s): ${data.artists.join(', ')}`;

    if (data.sources.length)
      caption += `\nSources: ${data.sources.map((source, i) => `[Source ${i}](${source}) ${(i + 1) !== data.sources.length ? '| ' : ''}`).join('')}`;

    const chatIDs = process.env.CHAT_IDS?.split(',') ?? [];
    for (let i = 0; i < chatIDs.length; i++) {
      const id = chatIDs[i];
      this.logger.info(`Posting yiff in chat ID "${id}"`);

      try {
        await this.telegram.sendPhoto(id, data.url, caption);
      } catch(ex) {
        this.logger.error(ex);
        this.telegram.sendMessage(id, `Unable to post yiff in this channel: ${ex.message} (Report this to @auguwu)`);
      }
    }
  }
}

const logger = new Logger('launcher');
async function main() {
  const bot = new AutoYiffPoster();

  logger.info('Booting up...');
  await bot.start();
}

main();
