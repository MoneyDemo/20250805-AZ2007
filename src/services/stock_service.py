"""
Business logic service for fetching stock data.
"""
from datetime import datetime
from twstock.realtime import get as get_realtime
from src.models.stock import Stock
from src.utils.errors import StockAPIError


class StockService:
    """
    Service layer for stock data retrieval using twstock.
    """
    def __init__(self) -> None:
        # Simple in-memory cache: code => Stock object
        self.cache: dict[str, Stock] = {}

    def get_stock(self, code: str) -> Stock:
        """
        Get stock data for the given code, optionally using cache.

        Args:
            code: Stock code string.

        Returns:
            Stock: Stock data model instance.

        Raises:
            StockAPIError: On invalid data or API failure.
        """
        try:
            # Check cache first
            if code in self.cache:
                return self.cache[code]

            result = get_realtime(code)
            if not result.get('success'):
                raise StockAPIError(f"Failed to fetch data for {code}", status_code=404)

            realtime = result.get('realtime', {})
            price_str = realtime.get('latest_trade_price')
            if price_str is None:
                raise StockAPIError(f"No price data for {code}", status_code=404)

            price = float(price_str)
            timestamp = datetime.now()

            stock = Stock(code=code, price=price, timestamp=timestamp)
            # Cache the result
            self.cache[code] = stock
            return stock

        except StockAPIError:
            raise
        except Exception as e:
            raise StockAPIError(str(e))
