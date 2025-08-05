"""
Application configuration settings.
This module contains all configuration classes for different environments.
"""
import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Base configuration class with common settings."""
    
    # Flask basic settings
    SECRET_KEY: str = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # Stock API settings
    AUTO_REFRESH_INTERVAL: int = int(os.environ.get('AUTO_REFRESH_INTERVAL', '10'))
    DEFAULT_STOCK_CODE: str = os.environ.get('DEFAULT_STOCK_CODE', '2330')
    
    # Request settings
    REQUEST_TIMEOUT: int = int(os.environ.get('REQUEST_TIMEOUT', '30'))
    
    @staticmethod
    def init_app(app) -> None:
        """Initialize application with configuration."""
        pass


class DevelopmentConfig(Config):
    """Development environment configuration."""
    
    DEBUG: bool = True
    TESTING: bool = False


class TestingConfig(Config):
    """Testing environment configuration."""
    
    DEBUG: bool = False
    TESTING: bool = True
    WTF_CSRF_ENABLED: bool = False


class ProductionConfig(Config):
    """Production environment configuration."""
    
    DEBUG: bool = False
    TESTING: bool = False


# Configuration mapping dictionary
config: dict = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
