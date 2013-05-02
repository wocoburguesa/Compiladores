from regex import RegEx
from tokenizer import *
from syntax import *
from utils import *

def test1():
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

def test2():
    a = Tokenizer('example2.js')
    a.make_tokens()
    a.print_all()

def test3():
    a = SyntaxAnalyzer('example2.js')
    a.load_grammar('grammar.js')
    a.print_all()
    return a

def test4():
    a = SyntaxAnalyzer('example2.js')
    a.load_grammar('grammar.js')
    a.make_table()
    return a

def test5():
    CSVTableReader.dict_from_table('table.csv')

def test6():
    a = SyntaxAnalyzer('example-correct.js')
    a.set_grammar('grammar.js', 'SC')
    a.load_table('table.csv')
    a.perform_analysis()
    return a

def test7():
    a = SyntaxAnalyzer('example-incorrect.js')
    a.set_grammar('grammar.js', 'SC')
    a.load_table('table.csv')
    a.perform_analysis()
    return a
