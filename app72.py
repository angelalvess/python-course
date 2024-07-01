def add_client(name, listt=None):
    if listt is None:
        listt = []
    listt.append(name)
    return listt


client1 = add_client('John')
add_client('Mary', client1)
print(client1)  # ['John']

client2 = add_client('Maria')
add_client('Mary', client2)
print(client2)  # ['John']

client3 = add_client('Angel')
add_client('Alves', client3)
print(client3)  # ['Maria', 'Mary']
