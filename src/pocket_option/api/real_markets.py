"""
Real markets API handler
"""

from typing import List
from src.pocket_option.models.asset import Asset

class RealMarketsAPI:
    """
    Real markets API handler
    """
    
    def __init__(self, client):
        """
        Initialize real markets API
        """
        self.client = client
    
    def get_assets(self) -> List[Asset]:
        """
        Get available real market assets
        """
        return self.client.get_real_markets_assets()
    
    def get_candles(self, asset: str, timeframe: str, count: int = 100):
        """
        Get candlestick data for real market asset
        """
        return self.client.get_candles(asset, timeframe, count, 'real')
