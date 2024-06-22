try:
    number = input("Enter a int number: ")
    number = int(number)

    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
except:
    print("You need to enter a number!")

try:
    hours = input("Enter the hours: ")
    hours = int(hours)

    if 0 <= hours <= 11:
        print("good morning")
    elif 12 <= hours <= 17:
        print("good afternoon")
    elif 18 <= hours <= 23:
        print("good night")
except:
    print("Invalid hour")


name = input("Enter your name: ")
name = len(name)

if name > 1 and name <= 4:
    print("Your name is too short")
elif name >= 4 and name <= 8:
    print("Your name is normal")
elif name >= 8:
    print("Your name is too long")
else:
    print("Invalid name")
