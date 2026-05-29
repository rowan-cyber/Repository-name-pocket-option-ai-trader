"""
Validation utilities
"""

def validate_email(email: str) -> bool:
    """
    Validate email format
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_position_size(size: float) -> bool:
    """
    Validate position size (0.01 to 10%)
    """
    return 0.01 <= size <= 0.10

def validate_asset_name(asset: str) -> bool:
    """
    Validate asset name format
    """
    return len(asset) > 0 and len(asset) <= 20
