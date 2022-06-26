from typing import Union
from typing import Type

from flask import Flask

from snippdev.user.resources import user_bp
from snippdev.extensions import db
from snippdev.extensions import bcrypt
from snippdev.extensions import cors
from snippdev.config import DevConfig
from snippdev.config import TestConfig
from snippdev.config import ProdConfig


def register_blueprints(app: Flask) -> None:
    """Register the Flask blueprints."""
    app.register_blueprint(user_bp)


def register_extensions(app: Flask) -> None:
    """Register the Flask extensions."""
    db.init_app(app)
    bcrypt.init_app(app)
    cors.init_app(app)


def create_app(
    config: Union[
        Type[DevConfig],
        Type[TestConfig],
        Type[ProdConfig],
    ] = ProdConfig
) -> Flask:
    """Create the Flask app through app factory pattern.
    https://flask.palletsprojects.com/en/2.1.x/patterns/appfactories/
    Config is defaulted to ProdConfig. All config possibilities are located in
    the config.py module.
    """
    app: Flask = Flask(__name__)
    app.config.from_object(config)

    register_blueprints(app)
    register_extensions(app)

    return app
