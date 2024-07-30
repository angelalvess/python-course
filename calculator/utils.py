import re

NUM_OR_DOT = re.compile(r'^[0-9.]$')


def isNumOrDot(s):
    return bool(NUM_OR_DOT.search(s))


def isValidNumber(s):
    valid = False

    try:
        float(s)
        valid = True
    except ValueError:
        valid = False
    return valid


def isEmpty(s):
    return s == ''
