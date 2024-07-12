def validar(f):
    def inner(x, y):
        if x < 0 or y < 0:
            raise ValueError('Os valores devem ser positivos')
        x *= 2
        y *= 2
        return f(x, y)
    return inner


@validar
def soma(x, y):
    return x + y


s1 = soma(1, 2)
print(s1)
