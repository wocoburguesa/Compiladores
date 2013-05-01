from exceptions import Exception

class InvalidToken(BaseException):
    def __init__(self, token_list):
        self.message = ''

        for token in token_list:
            self.message += 'On line %(line)d: %(message)s\n' % {
                'message': token.error,
                'line': token.line
                }

    def __str__(self):
        return repr(self.message)
