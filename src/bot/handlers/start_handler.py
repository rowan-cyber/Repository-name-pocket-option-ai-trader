"""
Start command handler
"""

from telegram import Update
from telegram.ext import ContextTypes

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Start command - initializes user and shows main menu
    """
    user = update.effective_user
    await update.message.reply_text(
        f"👋 Welcome {user.first_name}!\n\n"
        f"🤖 Pocket Option Telegram Bot\n\n"
        f"Available commands:\n"
        f"/market - Select market (Real/OTC)\n"
        f"/buy - Buy signal\n"
        f"/sell - Sell signal\n"
        f"/account - View account\n"
        f"/stats - View trading stats\n"
        f"/settings - Configure bot\n"
    )
