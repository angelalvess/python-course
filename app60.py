
def summ(x, y):
    return x+y


def multiply(x, y):
    return x*y


def create_function(function, x):
    def interna(y):
        return function(x, y)
    return interna


summ_with_five = create_function(summ, 5)
multiply_with_five = create_function(multiply, 5)

print(summ_with_five(10))
print(multiply_with_five(10))
