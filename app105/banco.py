import conta
import pessoa


class Banco:
    def __init__(
        self,
        agencias: list[int] | None = None,
        clientes: list[pessoa.Pessoa] | None = None,
        contas: list[conta.Conta] | None = None,
    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            return True
        return False

    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            return True
        return False

    def _checa_conta(self, conta):
        if conta in self.contas:
            return True
        return False

    def _checa_cliente_conta(self, cliente, conta):
        if cliente.conta == conta:
            return True
        return False

    def autenticar(self, cliente: pessoa.Pessoa, conta: conta.Conta,):
        return self._checa_cliente(cliente) and self._checa_conta(conta) and \
            self._checa_agencia(
                conta) and self._checa_cliente_conta(cliente, conta)

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attr = f'Agências: {self.agencias}, Clientes: {self.clientes}, '\
            f'Contas: {self.contas}'
        return f'{class_name}({attr})'


if __name__ == '__main__':
    cliente1 = pessoa.Cliente('Felicity', 21)
    conta_corrente = conta.ContaCorrente(123, 2222, 0, 100)
    cliente1.conta = conta_corrente
    banco1 = Banco()
    banco1.clientes.extend([cliente1])
    banco1.contas.extend([conta_corrente])
    banco1.agencias.extend([123])

    if banco1.autenticar(cliente1, conta_corrente):
        conta_corrente.depositar(20)
        print(cliente1.conta)
