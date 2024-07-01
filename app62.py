from itertools import zip_longest


l1 = ['Salvador', 'Bahia', 'Brasil']
l2 = ['São Paulo', 'São Paulo', 'Brasil',
      'Rio de Janeiro', 'Rio de Janeiro', 'Brasil']

print(list(zip(l1, l2)))
print(list(zip_longest(l1, l2)))
