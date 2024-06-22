for i in range(10):

    if i == 2:
        print("i is 2")
        continue

    if i == 5:
        print("i is 5")
        break

    for j in range(5, 11):
        print(j, i)
else:
    print("Loop is over")
