"""
Main Flask application factory.
This module creates and configures the Flask application.
"""
from flask import Flask
from config import config


def create_app(config_name: str = 'default') -> Flask:
    """
    Application factory for creating Flask app instances.

    Args:
        config_name: Configuration environment name

    Returns:
        Configured Flask application instance
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Register blueprints
    from src.routes.views import main_bp
    from src.routes.api import api_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
