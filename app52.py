product = {
    'name': 'book',
    'price': 3.99,
    'category': 'stationary',
}

dc = {
    key: value.upper()
    if isinstance(value, str)
    else value
    for key, value in product.items()
}

print(dc)
print("Open file", __name__)
