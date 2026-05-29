"""
Application constants
"""

# Trading constants
DEFAULT_EXPIRATION = 60  # 1 minute
MIN_POSITION_SIZE = 0.01  # 1%
MAX_POSITION_SIZE = 0.10  # 10%

# RSI constants
RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30

# MACD constants
MACD_FAST = 12
MACD_SLOW = 26
MACD_SIGNAL = 9

# Bollinger Bands constants
BB_PERIOD = 20
BB_STD_DEV = 2

# EMA constants
EMA_FAST = 9
EMA_SLOW = 21

# Market types
MARKET_REAL = 'real'
MARKET_OTC = 'otc'

# Trade directions
DIRECTION_BUY = 'buy'
DIRECTION_SELL = 'sell'

# Trade statuses
STATUS_PENDING = 'pending'
STATUS_WON = 'won'
STATUS_LOST = 'lost'
STATUS_CLOSED = 'closed'
