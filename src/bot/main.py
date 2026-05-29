"""
Main Pocket Option Telegram Bot Entry Point

This module initializes and runs the Telegram bot with all handlers and features.
"""

import logging
import os
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "src"))

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from src.config.settings import Settings
from src.logger.logger import setup_logger

# Setup logger
logger = setup_logger(__name__)

# Initialize settings
settings = Settings()

# Import handlers
try:
    from src.bot.handlers.start_handler import start_command
    from src.bot.handlers.markets_handler import market_command, market_callback
    from src.bot.handlers.trading_handler import buy_command, sell_command, trade_callback
    from src.bot.handlers.account_handler import account_command, stats_command
    from src.bot.handlers.strategy_handler import strategy_command, strategy_callback
    from src.bot.handlers.settings_handler import settings_command, settings_callback
    logger.info("✅ All handlers imported successfully")
except ImportError as e:
    logger.error(f"❌ Failed to import handlers: {e}", exc_info=True)
    sys.exit(1)

async def error_handler(update, context):
    """Handle errors in the bot"""
    logger.error(f"Error: {context.error}", exc_info=True)
    try:
        await context.bot.send_message(
            chat_id=update.effective_chat.id if update else "unknown",
            text="❌ An error occurred. Please try again later."
        )
    except Exception as e:
        logger.error(f"Failed to send error message: {e}")

async def post_init(application):
    """Post-initialization tasks"""
    logger.info("🚀 Bot initialization complete")
    logger.info(f"📊 Database: {settings.database_url}")
    logger.info(f"💰 Default position size: {settings.default_position_size * 100}%")
    logger.info(f"⏱️  Default expiration: {settings.default_expiration}s")
    logger.info(f"📈 Strategy: {settings.strategy_name}")
    
def main():
    """Main bot startup function"""
    logger.info("🔄 Starting Pocket Option Telegram Bot...")
    
    # Validate settings
    if not settings.telegram_bot_token:
        logger.error("❌ TELEGRAM_BOT_TOKEN not set in .env file")
        sys.exit(1)
    
    if not settings.pocket_option_email or not settings.pocket_option_password:
        logger.error("❌ Pocket Option credentials not set in .env file")
        sys.exit(1)
    
    # Create application
    app = Application.builder().token(settings.telegram_bot_token).build()
    
    # Add handlers
    logger.info("📋 Adding command handlers...")
    
    # Start command
    app.add_handler(CommandHandler("start", start_command))
    
    # Market commands
    app.add_handler(CommandHandler("market", market_command))
    app.add_handler(CallbackQueryHandler(market_callback, pattern="^market_"))
    
    # Asset/Trading commands
    app.add_handler(CommandHandler("buy", buy_command))
    app.add_handler(CommandHandler("sell", sell_command))
    app.add_handler(CallbackQueryHandler(trade_callback, pattern="^trade_"))
    
    # Account commands
    app.add_handler(CommandHandler("account", account_command))
    app.add_handler(CommandHandler("stats", stats_command))
    
    # Strategy commands
    app.add_handler(CommandHandler("strategy", strategy_command))
    app.add_handler(CallbackQueryHandler(strategy_callback, pattern="^strategy_"))
    
    # Settings commands
    app.add_handler(CommandHandler("settings", settings_command))
    app.add_handler(CallbackQueryHandler(settings_callback, pattern="^setting_"))
    
    # Error handler
    app.add_error_handler(error_handler)
    
    # Post-init
    app.post_init = post_init
    
    # Start bot
    logger.info("🎯 Bot is running...")
    logger.info(f"📱 Find your bot on Telegram or use bot token: {settings.telegram_bot_token[:20]}...")
    
    try:
        app.run_polling(allowed_updates=['message', 'callback_query'])
    except KeyboardInterrupt:
        logger.info("⏹️  Bot stopped by user")
    except Exception as e:
        logger.error(f"❌ Fatal error: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
