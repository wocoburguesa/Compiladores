import json

import constants
from tokenizer import Tokenizer
from utils import CSVTableReader

class SyntaxAnalyzer(object):

    def __init__(self, code_file):
        """
        code_file: code to compile
        grammar_file: json-encoded grammar
        """
        self.tokenizer = Tokenizer(code_file)
        self.tokenizer.make_tokens()

        self.table = None

    def load_grammar(self, grammar_file):
        grammar = open(grammar_file, 'r')
        self.grammar = json.loads(grammar.read())
        grammar.close()

    def make_table(self):
        terminals = {key:None for key in constants.TERMINALS}
        self.table = {key:terminals.copy() for key in self.grammar.keys()}

    def load_table(self, table_file):
        if not self.table:
            self.make_table()

        loaded_table = CSVTableReader.dict_from_table(table_file)

        for production in loaded_table.keys():
            for terminal in loaded_table[production].keys():
                production_choice = loaded_table[production][terminal]
                if production_choice != None:
                    self.table[production][terminal] = \
                        self.grammar[production][production_choice]

        self_keys = self.table['SC'].keys()
        self_keys.append('$')
        self_keys.sort()
        loaded_keys = loaded_table['SC'].keys()
        loaded_keys.sort()

        for a in range(len(self.table.keys())):
            print self_keys[a], loaded_keys[a]

        if loaded_keys == self_keys:
            print 'ok'


    def print_all(self):
        self.tokenizer.print_all()
