"""
Handles GPT-based text generation commands.
"""
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

class TextGenerationHandler:
    def __init__(self, app):
        self.app = app

    def register(self):
        self.app.add_handler(CommandHandler("generate", self.generate))

    def generate(self, update: Update, context: CallbackContext):
        # TODO: call NLP model, send result
        update.message.reply_text("🤖 Generating text…")
