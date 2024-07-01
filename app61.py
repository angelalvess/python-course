
def create_function(func):
    def intern(*args, **kwargs):
        for arg in args:
            is_string(arg)

        result = func(*args, **kwargs)
        return result
    return intern


@create_function
def invert_string(s):
    return s[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError("Only strings are allowed")


inverted = invert_string('123')
print(inverted)
