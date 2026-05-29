"""
OTC markets API handler
"""

from typing import List
from src.pocket_option.models.asset import Asset

class OTCMarketsAPI:
    """
    OTC markets API handler
    """
    
    def __init__(self, client):
        """
        Initialize OTC markets API
        """
        self.client = client
    
    def get_assets(self) -> List[Asset]:
        """
        Get available OTC market assets
        """
        return self.client.get_otc_markets_assets()
    
    def get_candles(self, asset: str, timeframe: str, count: int = 100):
        """
        Get candlestick data for OTC market asset
        """
        return self.client.get_candles(asset, timeframe, count, 'otc')
