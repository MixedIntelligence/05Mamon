# File: app/__init__.py
# Path: app/
# Description: Initializes the Flask application and sets up the SQLAlchemy database.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)

    with app.app_context():
        from app import routes  # Import routes to register them
        db.create_all()         # Create database tables

    return app
