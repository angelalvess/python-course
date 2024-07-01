import copy

produtos = [
    {'nome': 'p5', 'preco': 81.23},
    {'nome': 'p1', 'preco': 13},
    {'nome': 'p2', 'preco': 55.55},
    {'nome': 'p3', 'preco': 10.11},
    {'nome': 'p4', 'preco': 22},
]

novos_produtos = copy.deepcopy(produtos)

novos_produtos = [
    {**produto, 'preco': round(produto['preco'] * 1.1, 2)}
    for produto in produtos
    if produto['preco'] >= 10
]

print(*novos_produtos, sep='\n')
print("--------------------------------------------------")


def show_ordened_list(products):
    for item in products:
        print(item)


p1 = sorted(novos_produtos, key=lambda item: item['nome'])
p2 = sorted(novos_produtos, key=lambda item: item['preco'], reverse=False)


show_ordened_list(p1)
print("--------------------------------------------------")
show_ordened_list(p2)
