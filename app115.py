import os

path = os.path.join('/Users', 'angel', 'Desktop')

for pasta in os.listdir(path):
    caminho_completo_pasta = os.path.join(path, pasta)
    print(caminho_completo_pasta)
    print(pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue

    for imagem in os.listdir(caminho_completo_pasta):
        print(' ', imagem)
