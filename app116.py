import os
from itertools import count

path = os.path.join('/Users', 'angel', 'Desktop', 'teste')
counter = count()

for root, dirs, files in os.walk(path):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual:', root)

    for directory in dirs:
        print('  ', the_counter, ' Dir: ', directory)

    for file in files:
        print('  ', the_counter, ' File: ', file)
