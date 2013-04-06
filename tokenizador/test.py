from regex import RegEx

if __name__ == '__main__':
    a = RegEx()
    program = open('example.js')
    b = [word.strip() for word in program.readlines()]
    program.close()

    line_number = 1
    for test in b:
        print 'Line #%d: %s %s' % (line_number,
                                   test,
                                   a.process(test))
        line_number += 1

