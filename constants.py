RESERVED_WORDS = [
    'while',
    'if',
    'then',
    'else,'
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
    '=': 'equals',
    '{': 'open_curly',
    '}': 'close_curly',
    '[': 'open_bracket',
    ']': 'close_bracket',
    ',': 'comma',
    ':': 'colon',
    '+': 'plus',
    '-': 'minus',
    '*': 'times',
    '/': 'slash',
    '#': 'numeral',
    }

VARIABLE = 'var'
NUMBER = 'num'
SYMBOL = 'symbol'
INVALID = 'invalid'
INVALID_MESSAGE = '"%(word)s" Is not a valid token'
RESWORD = 'resword'
