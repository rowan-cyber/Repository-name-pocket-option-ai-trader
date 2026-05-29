"""
Asset model
"""

from dataclasses import dataclass
from typing import Optional

@dataclass
class Asset:
    """
    Asset model
    """
    symbol: str
    name: str
    market: str  # 'real' or 'otc'
    asset_type: str  # 'forex', 'crypto', 'commodity', 'index'
    min_investment: Optional[float] = None
    max_investment: Optional[float] = None
    is_active: bool = True
