while True:

    number_1 = input("Enter first number: ")
    number_2 = input("Enter second number: ")
    operator = input("Enter operator (+/-*): ")

    valid_numbers = None

    number_1_float = 0
    number_2_float = 0

    try:
        number_1_float = float(number_1)
        number_2_float = float(number_2)
        valid_numbers = True
    except:
        valid_numbers = None

    if valid_numbers is None:
        print("Invalid Numbers")
        continue

    valid_operators = "+-*/"

    if operator not in valid_operators:
        print("Invalid Operator")
        continue

    if len(operator) > 1:
        print("Just one operator is allowed")
        continue

    if operator == "+":
        print(f"Result: {number_1_float + number_2_float    }")
    elif operator == "-":
        print(f"Result: {number_1_float - number_2_float    }")
    elif operator == "*":
        print(f"Result: {number_1_float * number_2_float    }")
    elif operator == "/":
        print(f"Result: {number_1_float / number_2_float    }")
    else:
        print("Invalid Operator")

    out = input("Wanna quit? [y]es: ").lower().startswith("y")

    if out:
        print("Bye!")
        break
