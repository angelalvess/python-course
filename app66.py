

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

# com list comprehension
# new_products = [
#     product for product in products
#     if product['price'] > 10
# ]


def filter_price(product):
    return product['price'] > 15


new_products = filter(filter_price, products)

print_iterable(products)
print_iterable(new_products)
