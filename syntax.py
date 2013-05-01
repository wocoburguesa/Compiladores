import json

import constants
from tokenizer import Tokenizer

class SyntaxAnalyzer(object):

    def __init__(self, code_file):
        """
        code_file: code to compile
        grammar_file: json-encoded grammar
        """
        self.tokenizer = Tokenizer(code_file)
        self.tokenizer.make_tokens()

    def load_grammar(self, grammar_file):
        grammar = open(grammar_file, 'r')
        self.grammar = json.loads(grammar.read())
        grammar.close()

    def make_table(self):
        self.table = {}
        terminals = {key:None for key in constants.TERMINALS}
        for production in self.grammar.keys():
            self.table[production] = terminals

    def load_table(self, table_file):
        table = open(table_file, 'r')
        self.table = json.loads(table.read())
        table.close()

        

    def print_all(self):
        self.tokenizer.print_all()
