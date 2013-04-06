from regex import RegEx

if __name__ == '__main__':
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
