
# Multiplicador
def cria_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicate = cria_multiplicador(2)
triplicar = cria_multiplicador(3)

print(triplicar(5))


# saudar
def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao} {nome}'
    return saudar


saudar1 = criar_saudacao('Olá')

print(saudar1('Ana'))
