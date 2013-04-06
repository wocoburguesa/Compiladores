import json

import regex
import constants

class Record:
    def __init__(self,
                 line,
                 lexeme,
                 token,
                 memory,
                 value,
                 context
                 ):
        self.line = line
        self.lexeme = lexeme
        self.token = token
        self.memory = memory
        self.value = value
        self.context = context

class Tokenizer:
    def __init__(self, filename):
        self.file = open(filename)
        self.lexemes = []
        self.symbols = []

    def process_chunk(self, chunk, line_number):
        buff = ''
        flag = False
        for c in chunk:
            if c in constants.SYMBOLS:
                self.symbols.append(
                    Record(
                        line=line_number,
                        lexeme=c,
                        token=c,
                        memory=1,
                        value=c,
                        context=None
                        )
                    )
                if flag:
                    self.symbols.append(
                        Record(
                            line=line_number,
                            lexeme=buff,
                            token=constants.VARIABLE,
                            memory=128,
                            value=None,
                            context=None
                            )
                        )
                    buff = ''
            if 
                

    def process_line(self, line, line_number):
        chunks = line.split()
        

    def make_tokens(self, filename=None):
        if filename:
            self.file = open(filename)

        line_counter = 1
        for line.strip() in self.file.readlines():
            
