first_value = int(input("Enter the first value: "))
second_value = int(input("Enter the second value: "))


if first_value > second_value:
    print(
        f"The fisrt value: {first_value} is greater than second value: {second_value}"
    )
elif first_value == second_value:
    print("Both values are equal")
else:
    print(
        f"The second value: {second_value} is greater than fisrt value: {first_value}"
    )
