list_a = [1, 2, 3, 4, 5]
list_b = [10, 20, 30, 40, 50]
list_sum = [a + b for a, b in zip(list_a, list_b)]

print(list_sum)
