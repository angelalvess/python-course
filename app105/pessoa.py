
import conta


class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def idade(self) -> int:
        return self.__idade

    @idade.setter
    def idade(self, idade: int):
        self.__idade = idade

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attr = f'Nome: {self.nome}, Idade: {self.idade}'
        return f'{class_name}({attr})'


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: conta.Conta | None = None


if __name__ == '__main__':
    c1 = Cliente('Luiz', 32)
    c1.conta = conta.ContaCorrente(1111, 3333, 5000, 1000)
    print(c1)
    print(c1.conta)
    print('------------------')
    c2 = Cliente('Angel', 22)
    c2.conta = conta.ContaPoupanca(55, 3333, 5000)
    print(c2)
    print(c2.conta)
