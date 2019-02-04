from werkzeug.exceptions import HTTPException


class DMSException(HTTPException):
    pass


class NoContentException(DMSException):
    code = 204
    description = 'No Content'


class ResetContentException(DMSException):
    code = 205
    description = 'Reset Content'


class WrongAuthExcption(DMSException):
    code = 401
    description = 'Wrong Auth'


class ForbiddenException(DMSException):
    code = 403
    description = 'Forbidden'


class ApplyTimeException(DMSException):
    code = 409
    description = 'Can\'t Apply Time'


class BadRequestException(DMSException):
    code = 400
    description = 'Bad Parameter Request'
