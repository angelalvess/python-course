

# criando set direto com chaves
s1 = {'angel', 1, 2, 3, 'bird', 'cat', 'dog', 'elephant'}
print(s1)

# remove valores duplicados
s2 = {1, 1, 3, 4, 3, 3, 4}
print(s2)

s3 = set()
s3.add(1)
s3.add(2)

s3.update(('angel', 1, 2, 3))

s3.discard(5)

# s3.clear()

print(s3)

# ele limpa os valores duplicados mesmo que estejam em sets diferentes
s4 = s1 | s3
s5 = s1 & s3
print(s4)
print(s5)
