"""
Handles /task commands: create, update, list, reminders.
"""
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

class TaskManagementHandler:
    def __init__(self, app):
        self.app = app

    def register(self):
        self.app.add_handler(CommandHandler("task", self.task))

    def task(self, update: Update, context: CallbackContext):
        # TODO: delegate to storage, schedule reminders
        update.message.reply_text("📋 Task management coming soon!")
