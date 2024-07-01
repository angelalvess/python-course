from itertools import groupby


students = [
    {'nome': 'Pedro', 'nota': 'A'},
    {'nome': 'Maria', 'nota': 'B'},
    {'nome': 'João', 'nota': 'C'},
    {'nome': 'Ana', 'nota': 'A'},
    {'nome': 'Carlos', 'nota': 'D'},
    {'nome': 'Julia', 'nota': 'B'},
    {'nome': 'Marcos', 'nota': 'C'},
    {'nome': 'Mariana', 'nota': 'A'},
    {'nome': 'Paulo', 'nota': 'D'},
    {'nome': 'Patricia', 'nota': 'B'},


]


def ordena(item):
    return item['nota']


agrouped_students = sorted(students, key=ordena)

groups = groupby(agrouped_students, key=ordena)

for key, value in groups:
    print(f'Nota: {key}')
    for student in value:
        print(student)
