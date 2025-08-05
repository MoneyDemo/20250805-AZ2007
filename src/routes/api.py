"""
API routes for stock endpoints.
"""
from flask import Blueprint, request, jsonify
from src.services.stock_service import StockService
from src.utils.validators import validate_stock_code
from src.utils.errors import StockAPIError, handle_errors

api_bp = Blueprint('api', __name__)
service = StockService()

@api_bp.route('/stock/<code>', methods=['GET'])
@handle_errors
def get_stock(code: str):
    """Get stock data for the given code."""
    validate_stock_code(code)
    stock = service.get_stock(code)
    return jsonify(stock.to_dict()), 200

@api_bp.route('/stock/refresh', methods=['GET'])
@handle_errors
def refresh_stock():
    """Refresh stock data by clearing cache and fetching fresh info."""
    code = request.args.get('code')
    if not code:
        raise StockAPIError("Stock code is required for refresh", status_code=400)
    validate_stock_code(code)
    if code in service.cache:
        del service.cache[code]
    stock = service.get_stock(code)
    return jsonify(stock.to_dict()), 200
