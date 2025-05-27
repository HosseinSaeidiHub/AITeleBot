"""
Pre-built InlineKeyboardMarkup factories for menus.
"""
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    buttons = [
        [InlineKeyboardButton("Generate Text", callback_data="gen")],
        [InlineKeyboardButton("Tasks", callback_data="tasks")],
    ]
    return InlineKeyboardMarkup(buttons)
