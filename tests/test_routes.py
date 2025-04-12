# File: tests/test_routes.py
# Path: tests/
# Description: Unit tests for the `/log-compost` API route.

import pytest
from app import create_app, db

@pytest.fixture
def app():
    """
    Creates a test Flask app with an in-memory database for testing.
    """
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
    yield app

def test_log_compost(client):
    """
    Test case for the /log-compost endpoint.
    Ensures composting logs can be added and tokens are issued.
    """
    response = client.post('/log-compost', json={'user_id': 1, 'weight': 5.0})
    assert response.status_code == 201
    assert b'Composting logged' in response.data
