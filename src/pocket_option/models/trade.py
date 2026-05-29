"""
Trade model
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Trade:
    """
    Trade model
    """
    trade_id: str
    asset: str
    market: str  # 'real' or 'otc'
    direction: str  # 'buy' or 'sell'
    amount: float
    entry_price: float
    entry_time: datetime
    expiration_time: int  # seconds
    status: str  # 'pending', 'won', 'lost'
    exit_price: Optional[float] = None
    exit_time: Optional[datetime] = None
    profit_loss: Optional[float] = None
