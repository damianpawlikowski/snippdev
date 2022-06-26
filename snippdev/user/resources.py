from typing import TypeVar
from typing import Tuple

from flask import Blueprint
from flask_apispec import MethodResource
from flask_apispec import use_kwargs
from flask_apispec import marshal_with

from snippdev.user.serializers import user_schema
from snippdev.user.models import User


user_bp: Blueprint = Blueprint("user_bp", __name__, url_prefix="/api/user")


T = TypeVar("T", bound="UserResource")


@marshal_with(user_schema)
class UserResource(MethodResource):
    @use_kwargs(user_schema)
    def post(
        self: T, email: str, password: str
    ) -> Tuple[User, int]:
        user: User = User.create(
            email=email,
            password=password,
        )
        return user, 201


user_bp.add_url_rule("/", view_func=UserResource.as_view("user"))
