frase = (
    " O python é uma linguagem de programação de alto"
    " nível, interpretada,"
    "de script, imperativa, orientada a objetos, funcional"
    ", de tipagem dinâmica e forte. "
)


i = 0
quantidade_de_vezes = 0
letra_que_mais_se_repete = ""

while i < len(frase):

    frase_atual = frase[i]

    if frase_atual == " ":
        i += 1
        continue

    qtd_atual = frase.count(frase_atual)

    if quantidade_de_vezes <= qtd_atual:
        quantidade_de_vezes = qtd_atual

        letra_que_mais_se_repete = frase_atual

    i += 1


print(
    f"A letra que mais se repete é: ({letra_que_mais_se_repete}) e apareceu {quantidade_de_vezes}x"
)
