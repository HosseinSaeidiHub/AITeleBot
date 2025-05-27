"""
Extra user flows: menus, confirmations, inline keyboards.
"""
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, CallbackQueryHandler

class UserInteractionHandler:
    def __init__(self, app):
        self.app = app

    def register(self):
        self.app.add_handler(CallbackQueryHandler(self.button))

    def button(self, update: Update, context: CallbackContext):
        # TODO: handle inline keyboard presses
        query = update.callback_query
        query.answer()
        query.edit_message_text(text="You clicked a button!")
