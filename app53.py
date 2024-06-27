lista = [
    "Python", 1, 2, 3, 4, 5, "Java", "C++", "C#", "JavaScript", {
        "name": "book", "price": 3.99, "category": "stationary", }, {1, 2, 3, 4, 5, },
]

for item in lista:
    if isinstance(item, set):
        item.add(10)

        print(item)
