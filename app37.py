def soma(x, y, z=None):
    if z is None:
        return x + y
    return x + y + z


print(soma(2, 3))
print(soma(2, 3, 4))
