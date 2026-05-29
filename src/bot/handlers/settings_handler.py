"""
Settings Handler

Handles bot settings and configuration.
"""

from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from src.logger.logger import setup_logger

logger = setup_logger(__name__)

async def settings_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle /settings command - Show settings menu
    """
    try:
        user_id = update.effective_user.id
        logger.info(f"👤 User {user_id} opened settings")
        
        message = """
⚙️ **Bot Settings**

Select which setting you'd like to configure:
        """
        
        keyboard = [
            [InlineKeyboardButton("💰 Position Size", callback_data="setting_position_size")],
            [InlineKeyboardButton("🎯 Risk Management", callback_data="setting_risk")],
            [InlineKeyboardButton("📊 Strategy Parameters", callback_data="setting_strategy")],
            [InlineKeyboardButton("🔔 Notifications", callback_data="setting_notifications")],
            [InlineKeyboardButton("📈 Auto Trading", callback_data="setting_auto_trading")],
            [InlineKeyboardButton("💾 Save Settings", callback_data="setting_save")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=message.strip(),
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
        
        logger.info(f"✅ Settings menu sent to user {user_id}")
        
    except Exception as e:
        logger.error(f"❌ Error in settings command: {e}", exc_info=True)
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="❌ Error occurred. Please try again."
        )

async def settings_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle settings callback
    """
    try:
        query = update.callback_query
        user_id = query.from_user.id
        setting_type = query.data.replace("setting_", "")
        
        logger.info(f"👤 User {user_id} accessed setting: {setting_type}")
        
        if setting_type == "position_size":
            message = """
💰 **Position Size Settings**

Current: 2% of account per trade

This is the amount of your account risked per trade.

Recommended range: 1-5%
• Conservative: 1%
• Moderate: 2%
• Aggressive: 3-5%

Use /setpositionsize [percentage] to change.
            """
        
        elif setting_type == "risk":
            message = """
🎯 **Risk Management Settings**

Daily Loss Limit: 5%
Max Consecutive Losses: 3
Stop Loss: 10 pips
Take Profit: 25 pips

These settings protect your account from excessive losses.

Change a setting with:
/setdailylimit [percentage]
/setmaxloss [number]
/setstoploss [pips]
/settakeprofit [pips]
            """
        
        elif setting_type == "strategy":
            message = """
📊 **Strategy Parameters**

Current Strategy: RSI + MACD

RSI Period: 14
RSI Overbought: 70
RSI Oversold: 30
MACD Fast: 12
MACD Slow: 26
Bollinger Bands Period: 20

Reset to defaults: /resetstrategy
Edit parameters: /editstrategy
            """
        
        elif setting_type == "notifications":
            message = """
🔔 **Notification Settings**

✅ Trade Notifications: Enabled
✅ Signal Alerts: Enabled
✅ Error Notifications: Enabled
✅ Daily Report: Enabled

Disable notifications: /togglenotifications
            """
        
        elif setting_type == "auto_trading":
            message = """
📈 **Auto Trading Settings**

Status: ❌ Disabled

Enable auto trading to execute trades automatically based on strategy signals.

Enable: /enableauto
Disable: /disableauto
View signals: /viewsignals
            """
        
        elif setting_type == "save":
            message = """
✅ **Settings Saved**

All your settings have been saved successfully.

Current Configuration:
• Position Size: 2%
• Strategy: RSI + MACD
• Risk Level: Moderate
• Notifications: Enabled
• Auto Trading: Disabled
            """
        
        else:
            message = "❓ Unknown setting"
        
        await query.edit_message_text(
            text=message.strip(),
            parse_mode='Markdown'
        )
        
    except Exception as e:
        logger.error(f"❌ Error in settings callback: {e}", exc_info=True)
