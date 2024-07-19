import json
import os


NOME_ARQUIVO = "app119.json"
CAMINHO_ABSOLUTO = os.path.abspath(
    os.path.join(os.path.dirname(__file__), NOME_ARQUIVO))

print(CAMINHO_ABSOLUTO)

filme = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "movies": [
        {
            "title": "The Shawshank Redemption",
            "year": 1994
        },
        {
            "title": "The Godfather",
            "year": 1972
        }
    ]
}


print(json.dumps(filme, indent=4))

with open(CAMINHO_ABSOLUTO, "w") as arquivo:

    json.dump(filme, arquivo, indent=4, ensure_ascii=False)
    print("Arquivo json criado com sucesso!")

with open(CAMINHO_ABSOLUTO, "r") as arquivo:
    filme_json = json.load(arquivo)
    print(filme_json)
