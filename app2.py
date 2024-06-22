entrada = input("[1] para entrar e [2] para sair: ")
password = input("Digite a senha: ")

valid_password = "123456"

if entrada == "1" and password == valid_password:
    print("Bem vindo!")
elif entrada == "1" and password != valid_password:
    print("Senha inválida!")
elif entrada == "2":
    print("Saindo...")
else:
    print("Opção inválida!")
