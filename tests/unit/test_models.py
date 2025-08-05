"""
Unit tests for Stock data model.
"""
import pytest
from datetime import datetime
from src.models.stock import Stock


def test_to_dict():
    # Arrange
    code = '2330'
    price = 600.5
    timestamp = datetime(2025, 8, 5, 12, 0, 0)
    stock = Stock(code=code, price=price, timestamp=timestamp)

    # Act
    result = stock.to_dict()

    # Assert
    assert result['code'] == code
    assert isinstance(result['price'], float)
    assert abs(result['price'] - price) < 1e-6
    assert result['timestamp'] == timestamp.isoformat()
