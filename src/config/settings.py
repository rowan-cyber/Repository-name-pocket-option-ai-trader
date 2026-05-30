"""
Settings configuration for Pocket Option Telegram Bot
"""

import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """
    Application settings loaded from environment variables
    """
    
    # Telegram
    telegram_bot_token: str = os.getenv("TELEGRAM_BOT_TOKEN", "")
    
    # Pocket Option
    pocket_option_email: str = os.getenv("POCKET_OPTION_EMAIL", "")
    pocket_option_password: str = os.getenv("POCKET_OPTION_PASSWORD", "")
    
    # Database
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./pocket_option.db")
    
    # Trading Settings
    default_position_size: float = float(os.getenv("DEFAULT_POSITION_SIZE", "0.02"))  # 2%
    default_expiration: int = int(os.getenv("DEFAULT_EXPIRATION", "60"))  # 60 seconds
    daily_loss_limit: float = float(os.getenv("DAILY_LOSS_LIMIT", "0.05"))  # 5%
    max_consecutive_losses: int = int(os.getenv("MAX_CONSECUTIVE_LOSSES", "3"))
    
    # Strategy Settings
    strategy_name: str = os.getenv("STRATEGY_NAME", "rsi_macd_strategy")
    
    # RSI Settings
    rsi_period: int = int(os.getenv("RSI_PERIOD", "14"))
    rsi_overbought: int = int(os.getenv("RSI_OVERBOUGHT", "70"))
    rsi_oversold: int = int(os.getenv("RSI_OVERSOLD", "30"))
    
    # MACD Settings
    macd_fast: int = int(os.getenv("MACD_FAST", "12"))
    macd_slow: int = int(os.getenv("MACD_SLOW", "26"))
    macd_signal: int = int(os.getenv("MACD_SIGNAL", "9"))
    
    # Logging
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    log_file: str = os.getenv("LOG_FILE", "bot.log")
    
    # Feature Flags
    auto_trading_enabled: bool = os.getenv("AUTO_TRADING_ENABLED", "False").lower() == "true"
    paper_trading_enabled: bool = os.getenv("PAPER_TRADING_ENABLED", "False").lower() == "true"
    
    def __init__(self):
        """Initialize settings"""
        self._validate_required()
    
    def _validate_required(self):
        """Validate required settings"""
        if not self.telegram_bot_token:
            print("⚠️  WARNING: TELEGRAM_BOT_TOKEN not set in .env file")
        
        if not self.pocket_option_email:
            print("⚠️  WARNING: POCKET_OPTION_EMAIL not set in .env file")
        
        if not self.pocket_option_password:
            print("⚠️  WARNING: POCKET_OPTION_PASSWORD not set in .env file")

# Create singleton instance
settings = Settings()
