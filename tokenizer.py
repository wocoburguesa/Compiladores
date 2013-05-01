import json

from custom_exceptions import InvalidToken
from regex import *
import constants

class Error:
    def __init__(self,
                 line,
                 error
                 ):
        self.line = line
        self.error = error

class Token:
    def __init__(self,
                 line,
                 lexeme,
                 token,
                 pos
                 ):
        self.line = line
        self.lexeme = lexeme
        self.token = token
        self.pos = pos

class Symbol:
    def __init__(self,
                 line,
                 lexeme,
                 token,
                 memory,
                 value,
                 context,
                 pos
                 ):
        self.line = line
        self.lexeme = lexeme
        self.token = token
        self.memory = memory
        self.value = value
        self.context = context
        self.pos = pos

class Tokenizer:
    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.tokens = []
        self.symbols = []
        self.errors = []
        self.regex = RegEx()
        self.pos = 0

    def process_word(self, buff, line_number):
        word_type = self.regex.process(buff)
        if word_type  == constants.VARIABLE:
            self.symbols.append(
                Symbol(
                    line=line_number,
                    lexeme=buff,
                    token=constants.VARIABLE,
                    memory=128,
                    value=None,
                    context=None,
                    pos=self.pos
                    )
                )
        elif word_type == constants.NUMBER:
            self.tokens.append(
                Token(
                    line=line_number,
                    lexeme=buff,
                    token=constants.NUMBER,
                    pos=self.pos
                    )
                )
        elif word_type == constants.RESWORD:
            self.tokens.append(
                Token(
                    line=line_number,
                    lexeme=buff,
                    token=buff,
                    pos=self.pos
                    )
                )
        elif word_type == constants.INVALID:
            self.errors.append(
                Error(
                    line=line_number,
                    error=constants.INVALID_MESSAGE % {'word': buff},
                    )
                )

        self.pos += 1

    def process_chunk(self, chunk, line_number):
        buff = ''
        flag = False
        for c in chunk:
            if c in constants.SYMBOLS.keys():
                if flag:
                    self.process_word(buff, line_number)
                    buff = ''
                    flag = False
                self.tokens.append(
                    Token(
                        line=line_number,
                        lexeme=c,
                        token=constants.SYMBOLS[c],
                        pos=self.pos
                        )
                    )
                self.pos += 1
            else:
                flag = True
                buff += c
        if flag:
            self.process_word(buff, line_number)

    def process_line(self, line, line_number):
        chunks = line.split()
        for chunk in chunks:
            self.process_chunk(chunk, line_number)

    def make_tokens(self, filename=None):
        if filename:
            self.file = open(filename)

        line_counter = 1
        for line in self.file.readlines():
            line.strip()
            self.process_line(line, line_counter)
            line_counter += 1

        if len(self.errors) > 0:
            raise InvalidToken(self.errors)

    def print_all(self):
        print 'TOKENS'
        for token in self.tokens:
            print 'Line %(line)s\ttoken: %(token)s\tlexeme: %(lexeme)s\tpost: %(pos)s' % {
                'line': token.line,
                'token': token.token,
                'lexeme': token.lexeme,
                'pos': token.pos
                }

        print 'SYMBOLS'
        for symbol in self.symbols:
            print 'Line %(line)s\ttoken: %(token)s\tlexeme: %(lexeme)s\t %(memory)s\t %(value)s\tpos: %(pos)s' % {
                'line': symbol.line,
                'token': symbol.token,
                'lexeme': symbol.lexeme,
                'memory': symbol.memory,
                'value': symbol.value,
                'pos': symbol.pos
                }

        print 'ERRORS'
        for error in self.errors:
            print 'Line %(line)s\terror: %(error)s' % {
                'line': error.line,
                'error': error.error
                }
