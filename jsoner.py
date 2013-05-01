import json

if __name__ == '__main__':
    txt = open('gramatica.txt', 'r')
    _json = {}
    target = open('grammar.js', 'w')

    for line in txt.readlines():
        line = [a.strip() for a in line.split('->')]
        choices = line[1].split('|')
        _json[line[0]] = [a.split() for a in choices]

    target.write(json.dumps(_json, indent=4))
    txt.close()
    target.close()
