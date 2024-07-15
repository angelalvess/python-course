import abc


class Conta(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor: float) -> float:
        ...

    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f'Deposito de: {valor}')
        return self.saldo

    def detalhes(self, msg: str = '') -> None:
        print(f' O seu saldo é de R$ {self.saldo:.2f} ({msg})')

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attr = f'Agência: {self.agencia}, Conta: {self.conta}, '\
            f'Saldo: {self.saldo}'
        return f'{class_name}({attr})'


class ContaPoupanca(Conta):
    def sacar(self, valor: float) -> float:
        if self.saldo < valor:
            print('Saldo insuficiente')
            return self.saldo
        self.saldo -= valor
        self.detalhes(f'Saque de: {valor}')
        return self.saldo


class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: float = 0,
                 limite: float = 0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor: float) -> float:
        if self.saldo + self.limite < valor:
            print('Saldo ou Limite insuficiente')
            print(f'Seu saldo é: {self.saldo:.2f} limite: {self.limite:.2f}')
            return self.saldo
        self.saldo -= valor
        self.detalhes(f'Saque de: {valor}')
        return self.saldo

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attr = f'Agência: {self.agencia}, Conta: {self.conta}, '\
            f'Saldo: {self.saldo}, Limite: {self.limite}'
        return f'{class_name}({attr})'


if __name__ == '__main__':
    print('Conta Poupança')
    conta_poupanca = ContaPoupanca(1234, 5678)
    conta_poupanca.depositar(100)
    conta_poupanca.sacar(50)
    print('==========')
    print('Conta Corrente')
    conta_corrente = ContaCorrente(4321, 8765, 0, 100)
    conta_corrente.sacar(50)
    conta_corrente.sacar(40)
    conta_corrente.sacar(30)
