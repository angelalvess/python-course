class Client:
    def __init__(self, name):
        self.name = name
        self.enderecos = []

    def add_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero


client = Client('João')
client.add_endereco('Rua A', 123)
client.add_endereco('Rua B', 456)
client.listar_enderecos()
