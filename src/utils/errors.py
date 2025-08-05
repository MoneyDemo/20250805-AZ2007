"""
Custom error classes and error handling decorators.
"""
from functools import wraps
from flask import jsonify


class StockAPIError(Exception):
    """Base exception for stock API errors."""
    status_code: int = 500
    message: str = "An unexpected error occurred."

    def __init__(self, message: str | None = None, status_code: int | None = None) -> None:
        if message:
            self.message = message
        if status_code:
            self.status_code = status_code
        super().__init__(self.message)


def handle_errors(f):
    """
    Decorator to handle StockAPIError and return JSON response.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except StockAPIError as e:
            response = jsonify({"error": e.message})
            response.status_code = e.status_code
            return response
    return decorated_function
