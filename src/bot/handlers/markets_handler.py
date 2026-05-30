"""
Markets handler
"""

from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes

async def market_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Market selection command
    """
    keyboard = [
        [
            InlineKeyboardButton("📊 Real Markets", callback_data="market_real"),
            InlineKeyboardButton("🎰 OTC Markets", callback_data="market_otc")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Select market type:",
        reply_markup=reply_markup
    )

async def market_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Market selection callback
    """
    query = update.callback_query
    await query.answer()
    
    market_type = query.data.split("_")[1]
    await query.edit_message_text(
        text=f"✅ Selected: {market_type.upper()} market"
    )
