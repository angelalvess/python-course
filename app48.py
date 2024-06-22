
# kwargs

pessoa = {
    'nome': 'Alberto',
    'sobrenome': 'Silva',
}
dados = {
    'idade': 30,
    'sexo': 'M',
}

pessoa_completa = {**pessoa, **dados}
print(pessoa_completa)
