import json

import constants
from tokenizer import Tokenizer, Token
from utils import CSVTableReader

class Grammar(object):
    def __init__(self, grammar_file, initial=None):
        self.productions = None
        self.initial = None
        self.terminals = None
        self.non_terminals = None

        self.read_productions(grammar_file)
        self.set_terminals()
        self.set_non_terminals()
        self.set_initial(initial)

    def read_productions(self, filename):
        grammar = open(filename, 'r')
        self.productions = json.loads(grammar.read())
        grammar.close()

    def set_terminals(self):
        self.terminals = constants.TERMINALS

    def set_non_terminals(self):
        self.non_terminals = self.productions.keys()

    def set_initial(self, initial=None):
        if initial:
            self.initial = initial
        else:
            self.initial = self.non_terminals[0]

class SyntaxError(object):
    def __init__(self,
                 line,
                 error
                 ):
        self.line = line
        self.error = error

    def __repr__(self):
        return 'On line %d: %s' % (self.line, self.error)

class SyntaxAnalyzer(object):

    def __init__(self, code_file):
        """
        code_file: code to compile
        grammar_file: json-encoded grammar
        """
        self.tokenizer = Tokenizer(code_file)
        self.tokenizer.make_tokens()
        self.make_token_sequence()

        self.table = None

        self.errors = []

    def set_grammar(self, grammar_file, initial=None):
        self.grammar_full = Grammar(grammar_file, initial)
        self.grammar = self.grammar_full.productions

    def make_token_sequence(self):
        self.token_sequence = []
        position = 0
        total = len(self.tokenizer.tokens) + len(self.tokenizer.symbols)

        while position < total:
            if self.tokenizer.tokens and \
                    self.tokenizer.tokens[0].pos == position:
                self.token_sequence.append(self.tokenizer.tokens[0])
                self.tokenizer.tokens.pop(0)
            else:
                self.token_sequence.append(self.tokenizer.symbols[0])
                self.tokenizer.symbols.pop(0)
            position += 1

        self.token_sequence.append(
            Token(
                line=0,
                lexeme=constants.END_SYMBOL,
                token=constants.END_SYMBOL,
                pos=-1
                )
            )

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

    def perform_analysis(self):
        stack = [constants.END_SYMBOL, self.grammar_full.initial]
        if not self.token_sequence:
            self.make_token_sequence()

        sequence = self.token_sequence
        first_terminal = None
        production = None
        pop_count = 0

        while stack and sequence:
            print 'STACK:', stack
            print 'SEQUENCE', [a.get_terminal() for a in sequence]
            raw_input()

            first_terminal = sequence[0].get_terminal()
            production = None

            #Ask if a new production needs to be pushed into the pile
            if stack[-1] in self.grammar_full.non_terminals:
                #Ask if such a production exists on the table
                if self.table[stack[-1]][first_terminal]:
                    production = list(self.table[stack.pop()][first_terminal])
                    #Ask if it isn't an empty production
                    if not production == constants.EMPTY_PRODUCTION:
                        while production:
                            stack.append(production.pop()) #reversing production

                else:
                    self.add_error(stack[-1], first_terminal, sequence[0].line)
                    if pop_count < constants.POP_THRESHOLD:
                        sequence.pop(0)
                        pop_count += 1
                    else:
                        stack.pop()
                        pop_count = 0

            elif stack[-1] == first_terminal:
                stack.pop()
                sequence.pop(0) #sequence is NOT a stack, pops from the front

            else:
                self.add_error(stack[-1], first_terminal, sequence[0].line)
                print self.errors[-1]
                if pop_count < constants.POP_THRESHOLD:
                    sequence.pop(0)
                    pop_count += 1
                else:
                    stack.pop()
                    pop_count = 0

    def add_error(self, expected, actual, line):
        if expected is '$':
            expected = constants.END_OF_FILE
        self.errors.append(
            SyntaxError(
                line=line,
                error=constants.SYNTAX_ERROR % {
                    'expected': expected,
                    'actual': actual
                    }
                )
            )
        

    def print_all(self):
        self.tokenizer.print_all()
