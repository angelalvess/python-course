from functools import partial


def print_iterable(iterable):
    print(*list(iterable), sep='\n')
    print()


products = [
    {'name': 'p1', 'price': 13},
    {'name': 'p2', 'price': 55.55},
    {'name': 'p3', 'price': 5.59},
    {'name': 'p4', 'price': 22},
    {'name': 'p5', 'price': 81.23},


]


def increase_porcent(value, porcent):
    return round(value * porcent, 2)


increase_ten = partial(increase_porcent, porcent=1.5)

# com list comprehension
# new_products = [
#     {**product, 'price': increase_ten(product['price'])}
#     for product in products
# ]


def change_price(product):
    product['price'] = increase_ten(product['price'])
    return product


new_products = map(change_price, products)

print_iterable(products)
print_iterable(new_products)
