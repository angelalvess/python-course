import re

NUM_OR_DOT = re.compile(r'^[0-9.]$')


def isNumOrDot(s):
    return bool(NUM_OR_DOT.search(s))


def isEmptry(s):
    return s == ''
