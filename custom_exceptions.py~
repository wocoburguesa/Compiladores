from exceptions import Exception

class InvalidToken(BaseException):
    def __init__(self, token, line):
        self.message = 'Token "%s" at line %d is invalid' % (token, line)

    def __str__(self):
        return repr(self.message)
