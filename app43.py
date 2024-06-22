pessoa = {
    'nome': 'Prof. Alberto',

    'cursos': [
        {'nome': 'Python Fundamentos', 'linguagem': 'Python'},
        {'nome': 'Estatística', 'linguagem': 'R'},
        {'nome': 'Matemática', 'linguagem': 'Python'}
    ]
}

pessoa.setdefault('idade', 43)
pessoa.update({'idade': 44})
print(pessoa)

print(list(pessoa.keys()))

# print(pessoa.get('idade', 23))


for key, value in pessoa.items():
    print(key, value)
