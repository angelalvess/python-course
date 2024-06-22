def soma(*args):
    total = 0
    for numero in args:
        total += numero

    return total


def multiply(*args):
    total = 1
    for numero in args:
        total *= numero

    return total


multiply_1 = multiply(5, 5, 5, 5)
print(multiply_1)  # 15


def is_odd_or_even(number):
    if number % 2 == 0:
        return 'Even'
    return 'Odd'


odd_or_even = is_odd_or_even(6)

print(odd_or_even)  # Odd
