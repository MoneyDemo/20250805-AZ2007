"""
Pytest fixtures for the Flask application and test client.
"""
import pytest
from app import create_app
from config import config


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app('testing')
    return app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """A test runner for invoking Click commands."""
    return app.test_cli_runner()
