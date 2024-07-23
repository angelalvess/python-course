
import random

nomes = ['Ana', 'Maria', 'José', 'Pedro']
random.shuffle(nomes)
print(nomes)

novos_nomes = random.sample(nomes, k=3)
print(novos_nomes)

nomes_choice = random.choices(nomes, k=2)
print(nomes_choice)

nomes_choice = random.choices(nomes)
print(nomes_choice)
