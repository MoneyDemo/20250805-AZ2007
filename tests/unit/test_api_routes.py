"""
Unit tests for API routes.
"""
import pytest
from src.models.stock import Stock


def fake_get_realtime_success(code: str):
    return {'success': True, 'realtime': {'latest_trade_price': '150.0'}}


def fake_get_realtime_fail(code: str):
    return {'success': False}


@pytest.fixture(autouse=True)
def patch_realtime(monkeypatch):
    import src.services.stock_service as ss
    monkeypatch.setattr(ss, 'get_realtime', fake_get_realtime_success)
    yield


def test_get_stock_success(client):
    resp = client.get('/api/stock/2330')
    assert resp.status_code == 200
    data = resp.get_json()
    assert data['code'] == '2330'
    assert isinstance(data['price'], float)


def test_get_stock_invalid_code(client):
    resp = client.get('/api/stock/abcd')
    assert resp.status_code == 400


def test_refresh_stock_success(client):
    # First fetch to cache
    client.get('/api/stock/2330')
    resp = client.get('/api/stock/refresh?code=2330')
    assert resp.status_code == 200
    data = resp.get_json()
    assert data['code'] == '2330'


def test_refresh_stock_missing_code(client):
    resp = client.get('/api/stock/refresh')
    assert resp.status_code == 400
