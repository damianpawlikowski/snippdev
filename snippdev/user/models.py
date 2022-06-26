from typing import TypeVar
from typing import Any
from datetime import datetime

from snippdev.extensions import db
from snippdev.extensions import bcrypt
from snippdev.utils import IdentifierMixin


T = TypeVar("T", bound="User")


class User(db.Model, IdentifierMixin):
    __tablename__ = "users"

    email = db.Column(db.String(254), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow,
    )

    def __init__(self: T, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        # Plain text password is accepted in the initializer, so let's hash it.
        self.set_password(self.password)

    def set_password(self: T, password: str) -> None:
        """Bcrypt-hash and set user's password."""
        self.password = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self: T, password: str) -> bool:
        """Return True if the passed password matches stored hash, otherwise
        return False.
        """
        return bcrypt.check_password_hash(self.password, password)
