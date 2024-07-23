import locale
from datetime import datetime
import string
from pathlib import Path

CAMINHO = Path(__file__).parent / 'app124.txt'
print(CAMINHO)

locale.setlocale(locale.LC_ALL, '')


def converte_para_brl(valor: float) -> str:
    brl = locale.currency(valor, grouping=True)
    return brl


data = datetime(2021, 1, 1)

dados = dict(nome='Cliente', idade=30, peso=80.5,
             valor=converte_para_brl(1000.50),
             data=data.strftime('%d/%m/%Y'))


with open(CAMINHO, 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    template = string.Template(texto)
    print(template.substitute(dados))
