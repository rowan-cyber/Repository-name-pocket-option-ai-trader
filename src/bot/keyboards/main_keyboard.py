"""
Main keyboard for bot
"""

from telegram import ReplyKeyboardMarkup, KeyboardButton

def get_main_keyboard():
    """
    Get main menu keyboard
    """
    keyboard = [
        [KeyboardButton("📈 Select Market"), KeyboardButton("💰 View Account")],
        [KeyboardButton("📊 View Stats"), KeyboardButton("⚙️ Settings")],
        [KeyboardButton("❓ Help")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
