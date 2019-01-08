class DMSException(Exception):
    pass


class NoContentException(DMSException):
    def __str__(self):
        return 'No Content'


class AlreadyExistItemException(DMSException):
    def __str__(self):
        return 'Already Exist Item'


class ResetContentException(DMSException):
    def __str__(self):
        return 'Reset Content'


class WrongAuthExcption(DMSException):
    def __str__(self):
        return 'Wrong Student'


class ApplyTimeException(DMSException):
    def __str__(self):
        return 'Apply Time Exception'
