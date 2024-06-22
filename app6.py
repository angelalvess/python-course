name = input("Enter your name: ")
age = int(input("Enter your age: "))

if name and age:
    print(f"Seu nome é {name}")
    print(f"Seu nome invertido é {name[::-1]}")
    print(f"Seu nome tem {len(name)} letras")
    print(f"A primeira letra do seu nome é {name[0]}")
    print(f"A última letra do seu nome é {name[-1]}")
else:
    print("Você deixou campos em branco.")
