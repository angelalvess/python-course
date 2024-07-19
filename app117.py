import os
import shutil

HOME = os.path.expanduser("~")
DESKTOP = os.path.join(HOME, "Desktop")
PASTA_ORIGINAL = os.path.join(DESKTOP, "teste")
NOVA_PASTA = os.path.join(DESKTOP, "novapasta")

print(DESKTOP)
print(PASTA_ORIGINAL)
print(NOVA_PASTA)

shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)

# os.makedirs(NOVA_PASTA, exist_ok=True)


# for root, dirs, files in os.walk(PASTA_ORIGINAL):
#     for dir in dirs:
#         caminho_arquivo_novo = os.path.join(
#             root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir)
#         os.makedirs(caminho_arquivo_novo, exist_ok=True)

#     for file in files:
#         caminho_arquivo = os.path.join(root, file)
#         caminho_arquivo_novo = os.path.join(
#             root.replace(PASTA_ORIGINAL, NOVA_PASTA), file)
#         shutil.copy(caminho_arquivo, caminho_arquivo_novo)
