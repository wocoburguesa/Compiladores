from regex import RegEx
from tokenizer import *
from syntax import SyntaxAnalyzer

def test_1():
    a = RegEx()
    program = open('example.js')
    b = [word.strip() for word in program.readlines()]
    program.close()
    output = open('tokens.txt', 'a')

    line_number = 1
    for test in b:
        output.write('Line #%d: %s\t%s\n' % (
                line_number,
                test,
                a.process(test, line_number)))
        line_number += 1

    output.close()

def test_2():
    a = Tokenizer('example2.js')
    a.make_tokens()
    a.print_all()

def test_3():
    a = SyntaxAnalyzer('example2.js')
    a.load_grammar('grammar.js')
    a.print_all()
    return a

if __name__ == '__main__':
    test_3()
