/**
 * Yiff Autoposter for Telegram
 *
 * Copyright (c) August 2020-present
 */

import type { AutoYiffPoster } from '.';
import cron from 'node-cron';

export async function create(bot: AutoYiffPoster) {
  bot.logger.info('Created cron scheduler');

  await bot.sendYiff();
  return cron.schedule('*/30 * * * *', () => bot.sendYiff(), { timezone: 'America/Phoenix' });
}
