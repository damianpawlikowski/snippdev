"""Utilities module."""
from typing import TypeVar
from typing import Type

from marshmallow import Schema
from marshmallow import EXCLUDE

from snippdev.extensions import db


T = TypeVar("T", bound="IdentifierMixin")


class IdentifierMixin:
    """Mixin that adds integer "id" column declared as primary key to any
    SQLA declarative-mapped class.
    """
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)

    @classmethod
    def get_by_id(cls: Type[T], id: int) -> T:
        """Get a record by id from the session identity map. If not present,
        SELECT will be performed in order to locate it.
        ``record = Model.get_by_id(43)``
        """
        return db.session.get(cls, id)


class BaseSchema(Schema):
    """Base schema with common metadata to avoid constant repeating."""
    class Meta:
        strict = True
        unknown = EXCLUDE
