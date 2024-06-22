salas = [
    ['Angelica', 'Beto', 'Carlos'],
    ['David', 'Eduardo', 'Fernando'],
    ['Gustavo', 'Hugo', 'Ivan', ('Jose', 'Juan')]
]


# print(salas[2])
# print(salas[0][2])
# print(salas[2][3][1])

for sala in salas:
    for nome in sala:
        print(nome)
