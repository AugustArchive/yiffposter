/**
 * Yiff Autoposter for Telegram
 *
 * Copyright (c) August 2020-present
 *
 * File: src/logger.ts
 * Description: Simple class to prettify logging
 */

import type { AutoYiffPoster } from '.';
import { replaceMD } from './utils';

export interface RequestData {
  sources: string[];
  artists: string[];
  url: string;
}

export abstract class Repository {
  public owner: string;
  public bot!: AutoYiffPoster;
  public api: string;

  constructor(api: string, owner: string) {
    this.owner = replaceMD(owner) as string;
    this.api = replaceMD(api) as string;
  }

  init(bot: AutoYiffPoster) {
    this.bot = bot;
    return this;
  }

  abstract request(): Promise<RequestData>;
}
