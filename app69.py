

caminho_arquivo = 'arquivo.txt'

with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    arquivo.write('Olá, arquivo! \n')
    arquivo.write('Olá, arquivo!')
    print('fechando arquivo...')

with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
    print(arquivo.read())
