"""
Unit tests for StockService.
"""
import pytest
from datetime import datetime
from src.services.stock_service import StockService
from src.utils.errors import StockAPIError


def fake_get_realtime_success(code: str):
    """Fake get_realtime returns success with price"""
    return {'success': True, 'realtime': {'latest_trade_price': '123.45'}}


def fake_get_realtime_no_price(code: str):
    """Fake get_realtime returns success but no price"""
    return {'success': True, 'realtime': {}}


def fake_get_realtime_fail(code: str):
    """Fake get_realtime returns failure"""
    return {'success': False}


@ pytest.fixture
def service_success(monkeypatch):
    """Return StockService with successful API stubbed"""
    import src.services.stock_service as ss
    monkeypatch.setattr(ss, 'get_realtime', fake_get_realtime_success)
    return StockService()


def test_get_stock_success(service_success):
    # Act
    stock = service_success.get_stock('2330')

    # Assert
    assert stock.code == '2330'
    assert stock.price == 123.45
    assert '2330' in service_success.cache


def test_get_stock_cached(monkeypatch, service_success):
    # First call caches the result
    stock1 = service_success.get_stock('2330')

    # Now monkeypatch get_realtime to fail if called again
    import src.services.stock_service as ss
    monkeypatch.setattr(ss, 'get_realtime', fake_get_realtime_fail)

    # Act
    stock2 = service_success.get_stock('2330')

    # Assert cached value returned
    assert stock2 is stock1


def test_get_stock_no_price(monkeypatch):
    import src.services.stock_service as ss
    monkeypatch.setattr(ss, 'get_realtime', fake_get_realtime_no_price)
    service = StockService()

    with pytest.raises(StockAPIError) as excinfo:
        service.get_stock('2330')
    assert 'No price data' in str(excinfo.value)


def test_get_stock_fail(monkeypatch):
    import src.services.stock_service as ss
    monkeypatch.setattr(ss, 'get_realtime', fake_get_realtime_fail)
    service = StockService()

    with pytest.raises(StockAPIError) as excinfo:
        service.get_stock('2330')
    assert 'Failed to fetch data' in str(excinfo.value)
