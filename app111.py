
from datetime import datetime
from dateutil.relativedelta import relativedelta

valor_total = 1_000_000
data_emprestimo = datetime(2020, 12, 20)
delta_anos = relativedelta(years=5)
data_final = data_emprestimo + delta_anos

data_parcelas = []
data_parcela = data_emprestimo


while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=1)

numero_parcelas = len(data_parcelas)
valor_parcela = valor_total / numero_parcelas


for data in data_parcelas:
    print(data.strftime('%Y-%m-%d'), f'R${valor_parcela:,.2f}')

print(f'Número de parcelas: {numero_parcelas}')
print(f'Valor da parcela: R${valor_parcela:,.2f}')
print(f'Valor total: R${valor_total:,.2f}')
print(f'Data do empréstimo: {data_emprestimo.strftime("%Y-%m-%d")}')
print(f'Data da ultima parcela: {data_final.strftime("%Y-%m-%d")}')
