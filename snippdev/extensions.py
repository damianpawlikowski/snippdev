"""Extensions module. Each extension is initialized in the app factory located
in app.py module."""
from typing import TypeVar
from typing import Type
from typing import Any

from flask_sqlalchemy import Model
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS


T = TypeVar("T", bound="BaseModel")


# SQLA Object-Relational Mapping
class BaseModel(Model):
    """Base that adds conveience methods for the database operations."""
    @classmethod
    def create(cls: Type[T], commit: bool = True, **kwargs: Any) -> T:
        """Create a new record and save it to the database."""
        instance: T = cls(**kwargs)
        return instance.save(commit)

    def update(self: T, commit: bool = True, **kwargs: Any) -> T:
        """Update specific fields of the record."""
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return commit and self.save() or self

    def delete(self: T, commit: bool = True) -> bool:
        """Delete the record from the database."""
        db.session.delete(self)
        return commit and db.session.commit()

    def save(self: T, commit: bool = True) -> T:
        """Save the record to the database."""
        db.session.add(self)
        if commit:
            db.session.commit()
        return self


db: SQLAlchemy = SQLAlchemy(model_class=BaseModel)


# Bcrypt Hashing Algorithm
bcrypt: Bcrypt = Bcrypt()


# Cross-Origin Resource Sharing
cors: CORS = CORS()
