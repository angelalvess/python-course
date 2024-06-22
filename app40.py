def criar_saudacao(sadacao):
    def saudar(nome):
        return f'{sadacao} {nome}'
    return saudar


s1 = criar_saudacao('Olá')

for nomes in ['Ana', 'Maria', 'José']:
    print(s1(nomes))
