"""
Configuration loader. Parses .env or other sources.
"""
import os

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    MODEL_PATH = os.getenv("MODEL_PATH")
    REDIS_URL = os.getenv("REDIS_URL", "")
