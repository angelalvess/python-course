

try:
    a = 18
    b = 1
    c = a / b
except ZeroDivisionError:
    print('Division by zero is not allowed.')
except NameError:
    print('Name b is not defined.')
