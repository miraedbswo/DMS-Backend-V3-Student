from functools import wraps

from flask import request

from app.exception import BadRequestException


def json_type_validate(json_schema: dict):
    def decorator(fn):

        @wraps(fn)
        def wrapper(*args, **kwargs):
            json: dict = request.json
            if not json:
                raise BadRequestException()

            for key, type_ in json_schema.items():
                value = json.get(key)
                if type(value) is not type_:
                    break
            else:
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
GOINGOUT_POST_JSON = dict(goOutDate=str, returnDate=str, reason=str)
MUSIC_POST_JSON = dict(day=int, singer=str, musicName=str)
MUSIC_DELETE_JSON = dict(appyId=int)
STAY_POST_JSON = dict(value=int)

# Report
BUG_POST_JSON = dict(content=str)
FACILITY_POST_JSON = dict(room=int, content=str)
