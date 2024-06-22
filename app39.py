def saudacao(msg, name):
    return f'{msg} {name}'


def executa(funcao, *args):
    return funcao(*args)


executa_funcao = executa(saudacao, 'Olá, mundo!', 'Python')

print(executa_funcao)
