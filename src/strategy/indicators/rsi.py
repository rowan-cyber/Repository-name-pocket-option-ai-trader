"""
RSI Indicator Implementation

Relative Strength Index (RSI) for momentum analysis.
"""

def calculate_rsi(prices, period=14):
    """
    Calculate Relative Strength Index (RSI)
    
    Args:
        prices: List of prices
        period: RSI period (default 14)
    
    Returns:
        RSI value (0-100)
    """
    if len(prices) < period + 1:
        return None
    
    deltas = [prices[i] - prices[i-1] for i in range(1, len(prices))]
    seed = deltas[:period]
    
    up = sum([delta for delta in seed if delta > 0]) / period
    down = -sum([delta for delta in seed if delta < 0]) / period
    
    if down == 0:
        return 100
    
    rs = up / down
    rsi = 100 - (100 / (1 + rs))
    
    # Calculate remaining RSI values
    for delta in deltas[period:]:
        if delta > 0:
            up = (up * (period - 1) + delta) / period
            down = (down * (period - 1)) / period
        else:
            up = (up * (period - 1)) / period
            down = (down * (period - 1) + (-delta)) / period
        
        rs = up / down
        rsi = 100 - (100 / (1 + rs))
    
    return rsi

def is_rsi_signal(rsi, overbought=70, oversold=30):
    """
    Determine RSI signal
    
    Args:
        rsi: RSI value
        overbought: Overbought threshold (default 70)
        oversold: Oversold threshold (default 30)
    
    Returns:
        Signal: 'buy' (oversold), 'sell' (overbought), or None
    """
    if rsi is None:
        return None
    
    if rsi < oversold:
        return 'buy'
    elif rsi > overbought:
        return 'sell'
    return None
