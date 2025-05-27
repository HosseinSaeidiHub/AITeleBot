"""
Main orchestration: sets up the Updater, registers handlers, and starts polling.
"""
from telegram.ext import ApplicationBuilder
from .config import Config
from .handlers.base import register_handlers

class BotCore:
    def __init__(self, token: str):
        self.app = ApplicationBuilder().token(token).build()

    def run(self):
        register_handlers(self.app)
        self.app.run_polling()
