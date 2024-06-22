name = "angelalves"

i = 0

while i < len(name):
    letter = name[i]

    if letter == " ":
        break

    print(letter)
    i += 1
else:
    print("No space found")
