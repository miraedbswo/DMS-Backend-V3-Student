from enum import Enum
from functools import wraps

from flask import request

from app.context import context_property
from app.exception import BadRequestException


class PayloadLocation(Enum):
    ARGS = "args"
    JSON = "json"


def data_type_validate(data_schema: dict, payload_location: PayloadLocation = PayloadLocation.JSON):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            data = {}
            if payload_location is payload_location.JSON:
                data: dict = request.json
            elif payload_location is payload_location.ARGS:
                data: dict = request.args

            if not data:
                raise BadRequestException()

            for key, type_ in data_schema.items():
                value = data.get(key)
                if payload_location is payload_location.ARGS:
                    continue

                if type(value) is not type_:
                    break
            else:
                context_property.request_payload = data
                return fn(*args, **kwargs)
            raise BadRequestException()

        return wrapper

    return decorator


# Account
AUTH_POST_JSON = dict(id=str, password=str)
PW_PATCH_JSON = dict(currentPassword=str, newPassword=str)
PW_POST_JSON = dict(id=str, email=str)
SIGNUP_POST_JSON = dict(uuid=str, id=str, password=str)

# Apply
EXTENSION_POST_JSON = dict(classNum=int, seatNum=int)
GOINGOUT_DELETE_JSON = dict(applyId=int)
GOINGOUT_POST_JSON = dict(date=str, reason=str)
GOINGOUT_PATCH_JSON = dict(applyId=int, date=str, reason=str)
MUSIC_POST_JSON = dict(day=int, singer=str, musicName=str)
MUSIC_DELETE_JSON = dict(applyId=int)
STAY_POST_JSON = dict(value=int)

# Report
BUG_POST_JSON = dict(content=str)
FACILITY_POST_JSON = dict(room=int, content=str)
