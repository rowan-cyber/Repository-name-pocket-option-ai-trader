"""
Market model
"""

from dataclasses import dataclass
from typing import List

@dataclass
class Market:
    """
    Market model
    """
    name: str
    market_type: str  # 'real' or 'otc'
    description: str
    is_active: bool = True
