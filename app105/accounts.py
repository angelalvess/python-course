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
        self.detalhes(f'Deposito de {valor}')
        return self.saldo

    def detalhes(self, msg: str = '') -> None:
        print(f' O seu saldo é de R${self.saldo:.2f} {msg}')


class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_apos_saques = self.saldo - valor

        if valor_apos_saques > 0:
            self.saldo -= valor
            self.detalhes(f'Saque de {valor}')
            return self.saldo

        print('Saldo insuficiente')
        self.detalhes(f'Saque negado de R${valor:.2f}')
        return self.saldo


class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: float = 0,
                 limite: float = 0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor: float) -> float:
        valor_apos_saques = self.saldo - valor
        limite_max = -self.limite

        if valor_apos_saques > limite_max:
            self.saldo -= valor
            self.detalhes(f'Saque de {valor}')
            return self.saldo

        print('Saldo insuficiente')
        print(f'Seu limite é de R${-self.limite:.2f}')
        self.detalhes(f'Saque negado de R${valor:.2f}')
        return self.saldo


if __name__ == '__main__':
    print('Conta Poupança')
    conta_poupanca = ContaPoupanca(1111, 2222)
    conta_poupanca.depositar(10)
    conta_poupanca.sacar(5)
    conta_poupanca.sacar(6)
    print('-----------------')
    print('Conta Corrente')
    conta_corrente = ContaCorrente(1111, 3333, 0, 100)
    conta_corrente.depositar(10)
    conta_corrente.sacar(115)
