"""
Market selection keyboard
"""

from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def get_market_keyboard():
    """
    Get market selection keyboard
    """
    keyboard = [
        [
            InlineKeyboardButton("📊 Real Markets", callback_data="market_real"),
            InlineKeyboardButton("🎰 OTC Markets", callback_data="market_otc")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
