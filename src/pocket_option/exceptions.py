"""
Pocket Option exceptions
"""

class PocketOptionException(Exception):
    """
    Base exception for Pocket Option
    """
    pass

class AuthenticationError(PocketOptionException):
    """
    Authentication failed
    """
    pass

class APIError(PocketOptionException):
    """
    API error
    """
    pass

class InsufficientFundsError(PocketOptionException):
    """
    Insufficient funds
    """
    pass

class AssetNotFoundError(PocketOptionException):
    """
    Asset not found
    """
    pass
