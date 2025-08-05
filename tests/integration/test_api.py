"""
Integration tests for the stock API endpoints.
"""
import pytest
from datetime import datetime

# Stub twstock realtime get for integration tests
@pytest.fixture(autouse=True)
def patch_twstock(monkeypatch):
    import twstock.realtime as tr

    def fake_get(code: str):
        return {'success': True, 'realtime': {'latest_trade_price': '999.99'}}

    monkeypatch.setattr(tr, 'get', fake_get)
    yield


def test_get_stock_success(client):
    resp = client.get('/api/stock/2330')
    assert resp.status_code == 200
    data = resp.get_json()
    assert data['code'] == '2330'
    assert data['price'] == 999.99


def test_get_stock_not_found(client):
    # Simulate failure by patching get to return success=False
    import twstock.realtime as tr
    tr.get = lambda code: {'success': False}
    resp = client.get('/api/stock/0000')
    assert resp.status_code == 404


def test_refresh_stock(client):
    # First query to set cache
    client.get('/api/stock/2330')
    # Refresh
    resp = client.get('/api/stock/refresh?code=2330')
    assert resp.status_code == 200
    data = resp.get_json()
    assert data['code'] == '2330'


def test_refresh_missing_code(client):
    resp = client.get('/api/stock/refresh')
    assert resp.status_code == 400
