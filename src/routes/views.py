"""
Page routes for frontend views.
"""
from flask import Blueprint, render_template, current_app

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Render the index page with default stock code."""
    default_code = current_app.config.get('DEFAULT_STOCK_CODE', '')
    return render_template('index.html', default_code=default_code)

@main_bp.app_errorhandler(404)
def page_not_found(e):
    """Render error page for 404 errors."""
    return render_template('error.html', message='Page not found'), 404

@main_bp.app_errorhandler(500)
def internal_error(e):
    """Render error page for internal server errors."""
    return render_template('error.html', message='Internal server error'), 500
