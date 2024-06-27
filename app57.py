try:
    print('Open file')
    8/0
except ZeroDivisionError:
    print('Division by zero is not allowed.')
finally:
    print('Close file')
