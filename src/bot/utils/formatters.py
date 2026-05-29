"""
Formatting utilities
"""

def format_price(price: float, decimals: int = 4) -> str:
    """
    Format price with specified decimals
    """
    return f"{price:.{decimals}f}"

def format_currency(amount: float) -> str:
    """
    Format amount as currency
    """
    return f"${amount:,.2f}"

def format_percentage(value: float) -> str:
    """
    Format value as percentage
    """
    return f"{value * 100:.2f}%"

def format_pnl(pnl: float) -> str:
    """
    Format profit/loss with color emoji
    """
    if pnl > 0:
        return f"🟢 +${pnl:.2f}"
    elif pnl < 0:
        return f"🔴 -${abs(pnl):.2f}"
    else:
        return f"⚪ ${pnl:.2f}"
