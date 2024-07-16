# from collections import namedtuple
from typing import NamedTuple


class Carta(NamedTuple):
    valor: str = 'valor'
    naipe: str = 'naipe'


as_carta = Carta('100', 'copas')
print(as_carta)

# Carta = namedtuple('Carta', ['valor', 'naipe'])
# print(Carta)
# print(Carta(10, 'copas'))
