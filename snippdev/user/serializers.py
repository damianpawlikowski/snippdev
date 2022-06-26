from typing import TypeVar

from marshmallow import fields
from marshmallow import validate
from marshmallow import validates
from marshmallow import ValidationError

from snippdev.utils import BaseSchema
from snippdev.user.models import User


T = TypeVar("T", bound="UserSchema")


class UserSchema(BaseSchema):
    email = fields.Email(required=True)
    password = fields.Str(
        required=True, load_only=True, validate=validate.Length(8, 72)
    )
    created_at = fields.DateTime(dump_only=True)

    @validates("email")
    def validate_email_uniqueness(self: T, email: str) -> None:
        """Validate if schema loaded e-mail is not being used by another
        user.
        """
        user: User = User.query.filter(User.email == email).first()
        if user is not None:
            raise ValidationError("This e-mail is already being used.")
        return None


user_schema: UserSchema = UserSchema()
