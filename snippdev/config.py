"""Config module."""
from typing import Optional
import os


class BaseConfig:
    """Base for all kind of configs."""
    SECRET_KEY: Optional[str] = os.environ.get("SNIPPDEV_SECRET_KEY")

    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    SQLALCHEMY_DATABASE_URI: Optional[str] = os.environ.get(
        'SNIPPDEV_DATABASE_URI'
    )


class DevConfig(BaseConfig):
    """Development config."""
    DEBUG: bool = True
    ENV: str = "development"


class TestConfig(BaseConfig):
    """Testing config."""
    TESTING: bool = True
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///:memory:"


class ProdConfig(BaseConfig):
    """Production config."""
    ENV: str = "production"
    GENERATE_SWAGGER_DOCS: bool = False
