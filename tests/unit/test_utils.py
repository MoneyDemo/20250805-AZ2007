"""
Unit tests for utility functions and error handling.
"""
import pytest
from datetime import datetime
from src.utils.validators import validate_stock_code
from src.utils.errors import StockAPIError, handle_errors

# Tests for validate_stock_code
@ pytest.mark.parametrize("code", ["2330", "2330.TW", "0050.TW"])
def test_validate_stock_code_valid(code):
    # Should not raise for valid codes
    validate_stock_code(code)

@ pytest.mark.parametrize("code", ["abc", "123", "12345", "233.TW"])
def test_validate_stock_code_invalid(code):
    with pytest.raises(StockAPIError) as excinfo:
        validate_stock_code(code)
    assert excinfo.value.status_code == 400
    assert "Invalid stock code format" in str(excinfo.value)

# Tests for handle_errors decorator
def test_handle_errors_decorator():
    # Create a dummy function that raises StockAPIError
    @handle_errors
    def view_func():
        raise StockAPIError("test error", status_code=418)

    # Call the decorated function
    response = view_func()
    # The decorator should return a Flask response object
    assert response.status_code == 418
    json_data = response.get_json()
    assert json_data.get("error") == "test error"
