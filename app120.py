from pathlib import Path
import csv

CAMINHO_CSV = Path(__file__).parent / 'app120.csv'


with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.reader(arquivo)

    for linha in leitor:
        print(linha)
