from regex import RegEx

if __name__ == '__main__':
    a = RegEx()
    b = [
        'hola',
        '_hola',
        'hol7a',
        '_ho89a',
        '_938',
        '8dj',
        'for',
        'while',
        '*',
        '}',
        '34s',
        '33.33',
        '33.33s',
        '33.33.',
        '_33.33'
        ]
    for test in b:
        print test
        print a.process(test)
