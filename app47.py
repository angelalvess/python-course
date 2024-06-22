listt = [
    {'name': 'Juan', 'city': 'Bogotá'},
    {'name': 'Pedro', 'city': 'Medellín'},
    {'name': 'Ana', 'city': 'Bogotá'},
    {'name': 'Luis', 'city': 'Cali'},
    {'name': 'María', 'city': 'Bogotá'},
    {'name': 'Carlos', 'city': 'Medellín'},
    {'name': 'Andrés', 'city': 'Cali'}
]


def show_ordened_list(listtt):
    for item in listtt:
        print(item)


l1 = sorted(listt, key=lambda item: item['name'])
l2 = sorted(listt, key=lambda item: item['city'])

show_ordened_list(l1)
print()
show_ordened_list(l2)


def execute(func, *args):
    return func(*args)


print(execute(lambda x, y: x + y, 10, 20))
