class DjBookshelfException(Exception):
    pass


class ISBNNoBookFoundException(DjBookshelfException):
    pass


class ISBNJsonException(DjBookshelfException):
    pass
