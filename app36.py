def summ(x, y):
    return x + y


def mult(x, y):
    return x * y


def welcome(name='user', age=1):
    return f'Hello, {name}! How are you? You are {age} years old.'


print(welcome(age=25, name='Angel'))
print(welcome())

print(summ(2, 3))
print(mult(2, 3))
