"""
Stock data model module.
"""
from datetime import datetime
from typing import Any


class Stock:
    """
    Represents a stock quote with code, price, and timestamp.

    Attributes:
        code (str): Stock ticker code.
        price (float): Latest stock price.
        timestamp (datetime): Time when the price was fetched.
    """
    def __init__(self, code: str, price: float, timestamp: datetime) -> None:
        self.code: str = code
        self.price: float = price
        self.timestamp: datetime = timestamp

    def to_dict(self) -> dict[str, Any]:
        """Convert the Stock object to a serializable dictionary."""
        return {
            "code": self.code,
            "price": self.price,
            "timestamp": self.timestamp.isoformat()
        }
