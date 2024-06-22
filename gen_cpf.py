import random


for i in range(25):

    nine_digits = ''

    for i in range(9):
        nine_digits += str(random.randint(0, 9))

    regressive_accumulator = 10

    result_1 = 0
    for digit in nine_digits:
        result_1 += int(digit) * regressive_accumulator

        regressive_accumulator -= 1

    first_digit = result_1 * 10 % 11
    first_digit = first_digit if first_digit <= 9 else 0

    ten_digits = nine_digits + str(first_digit)
    regressive_accumulator_2 = 11

    result_2 = 0
    for digit in ten_digits:
        result_2 += int(digit) * regressive_accumulator_2

        regressive_accumulator_2 -= 1

    second_digit = result_2 * 10 % 11
    second_digit = second_digit if second_digit <= 9 else 0

    new_id = f'{nine_digits}{first_digit}{second_digit}'

    print(f'CPF: {new_id}')
