"""
Validation utility functions.
"""
import re
from src.utils.errors import StockAPIError


def validate_stock_code(code: str) -> None:
    """
    Validate the stock code format for Taiwan stock.

    Args:
        code: Stock code string.

    Raises:
        StockAPIError: If the code format is invalid.
    """
    if not re.fullmatch(r"^\d{4}(\.TW)?$", code):
        raise StockAPIError(f"Invalid stock code format: {code}", status_code=400)
