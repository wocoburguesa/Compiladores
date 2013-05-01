import json
import sys

"""
Takes a .txt grammar file and saves it in JSON format
"""

if __name__ == '__main__':
    txt = open(sys.argv[1], 'r')
    _json = {}
    target = open(sys.argv[2], 'w')

    for line in txt.readlines():
        line = [a.strip() for a in line.split('->')]
        choices = line[1].split('|')
        _json[line[0]] = [a.split() for a in choices]

    target.write(json.dumps(_json, indent=4))
    txt.close()
    target.close()
