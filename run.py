#!/usr/bin/env python
"""
Simple runner script for the Pocket Option Telegram Bot
Run from project root: python run.py
"""

import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Now import and run the bot
from src.bot.main import main

if __name__ == "__main__":
    main()
