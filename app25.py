list_1 = [1, 2, 3]
list_2 = list_1.copy()

list_1.append(4)
list_1[0] = 5

print(list_1)
print(list_2)


for i in list_1:
    print(i)
