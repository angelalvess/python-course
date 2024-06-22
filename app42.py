# dict

pessoa = {
    'nome': 'Prof. Alberto',
    'idade': 43,
    'cursos': [
        {'nome': 'Python Fundamentos', 'linguagem': 'Python'},
        {'nome': 'Estatística', 'linguagem': 'R'},
        {'nome': 'Matemática', 'linguagem': 'Python'}
    ]
}

print(pessoa['nome'])
print(pessoa['cursos'][2])
print(pessoa['cursos'][2]['linguagem'])
print(pessoa.keys())
print(pessoa.values())

print('-----------------------------')

for chave in pessoa.items():
    print(*chave)
