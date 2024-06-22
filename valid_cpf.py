import re
import sys

entrada = input('Digite o CPF: ')
cpf = re.sub(r'[^0-9]', '', entrada)


entrada_repetida = entrada == entrada[0] * len(entrada)

if entrada_repetida:
    print('Você enviou dados sequenciais, por favor, envie dados válidos.')
    sys.exit()

nine_digits = cpf[:9]

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

if cpf == new_id:
    print('CPF válido')
else:
    print('CPF inválido')
