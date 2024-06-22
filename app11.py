condition = True

while condition:
    name = input("Please enter your name: ")
    print("Hello", name)

    if name == "stop":
        print("Goodbye", name)
        break
