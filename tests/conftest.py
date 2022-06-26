"""Tests config module."""
import pytest

from snippdev.app import create_app
from snippdev.config import TestConfig
from snippdev.extensions import db


@pytest.fixture
def app():
    """The Flask app for tests."""
    _app = create_app(TestConfig)
    with _app.app_context():
        db.create_all()
    return _app


@pytest.fixture
def client(app):
    """The Flask test client for tests."""
    return app.test_client()
