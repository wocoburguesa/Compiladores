RESERVED_WORDS = [
    'while',
    'if',
    'then',
    'else',
    'args',
    'return',
    'and',
    'or',
    'not',
    'function',
    'none'
    ]

SYMBOLS = {
    '>': 'greater_than',
    '<': 'lesser_than',
    '==': 'equals',
    '<=': 'lessereq',
    '>=': 'greatereq',
    '{': 'open_curly',
    '}': 'close_curly',
    '[': 'open_bracket',
    ']': 'close_bracket',
    ',': 'comma',
    ':': 'colon',
    '+': 'plus',
    '-': 'minus',
    '*': 'times',
    '/': 'slash'
    }

VARIABLE = '<var>'
NUMBER = '<num>'

TERMINALS = RESERVED_WORDS + SYMBOLS.keys() + [VARIABLE, NUMBER]

SYMBOL = 'symbol'
INVALID = 'invalid'
LEXICAL_ERROR = '"%(word)s" Is not a valid token'
RESWORD = 'resword'

#Syntax
EMPTY_PRODUCTION = ['e']
END_SYMBOL = '$'
SYNTAX_ERROR = 'Expected %(expected)s, got "%(actual)s" instead'
END_OF_FILE = 'end of file'
POP_THRESHOLD = 2
