from functools import reduce

products = [
    {'name': 'p1', 'price': 13},
    {'name': 'p2', 'price': 55.55},
    {'name': 'p3', 'price': 5.59},
    {'name': 'p4', 'price': 22},
    {'name': 'p5', 'price': 81.23},
]


def func_reduce(acc, product):
    return acc + product['price']


total = reduce(func_reduce, products, 0)

print(total)
