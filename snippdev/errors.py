"""Module containing error handlers."""
from typing import Optional
from typing import Any
from typing import Mapping
from typing import NoReturn

from webargs.flaskparser import parser
from webargs.core import Request

from flask import Response
from flask import jsonify
from flask import abort

from marshmallow import ValidationError
from marshmallow import Schema


def error_response(
    error_status_code: int,
    msg: Optional[str] = None,
    data: Optional[Any] = None
) -> Response:
    """Basic API error response."""
    payload: dict[str, Any] = {
        "msg": msg,
        "data": data,
    }

    response: Response = jsonify(payload)
    response.status_code = error_status_code

    return response


@parser.error_handler
def handle_request_parsing_error(
    error: ValidationError,
    request: Request,
    schema: Schema,
    *,
    error_status_code: int,
    error_headers: Mapping[str, str]
) -> NoReturn:
    """Custom error handler aborting request with Marshmallow's
    ValidationError messages in the JSON fromat."""
    # https://github.com/jmcarp/flask-apispec/issues/139
    # There is an issue, where error_status_code is not passed to
    # parser.error_handler. This is avaliable workaround:
    _error_status_code: int = error_status_code or 422

    response: Response = error_response(
        _error_status_code,
        # Skip useless "json" prefix
        data=error.messages.get("json"),  # type: ignore
    )
    abort(response)
