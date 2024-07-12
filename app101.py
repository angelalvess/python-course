class Multiply:
    ...

    def __init__(self, func):
        self.func = func
        self._multiply = 5

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        return result * self._multiply


@Multiply
def summ(x, y):
    return x + y


print(summ(1, 2))
