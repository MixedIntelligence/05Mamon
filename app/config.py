# File: app/config.py
# Path: app/
# Description: Configuration settings for the Flask application.

class Config:
    """
    Configuration class for Flask app.
    Includes database URI and other settings.
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/mamon_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
