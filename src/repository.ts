/**
 * Yiff Autoposter for Telegram
 *
 * Copyright (c) August 2020-present
 *
 * File: src/logger.ts
 * Description: Simple class to prettify logging
 */

import type { AutoYiffPoster } from '.';

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
    this.owner = owner;
    this.api = api;
  }

  init(bot: AutoYiffPoster) {
    this.bot = bot;
    return this;
  }

  abstract request(): Promise<RequestData>;
}
