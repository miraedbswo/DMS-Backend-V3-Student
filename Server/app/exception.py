class DMSException(Exception):
    pass


class NoContentException(DMSException):
    def __str__(self):
        return 'No Content'


class AlreadyExistItemException(DMSException):
    def __str__(self):
        return 'Already Exist Item'
