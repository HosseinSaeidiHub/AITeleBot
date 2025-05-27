#!/usr/bin/env python3
"""
Entry point: load config, initialize BotCore, and start polling.
"""
import os
from dotenv import load_dotenv
from bot.core import BotCore

def main():
    load_dotenv()
    token = os.getenv("BOT_TOKEN")
    core = BotCore(token)
    core.run()

if __name__ == "__main__":
    main()
