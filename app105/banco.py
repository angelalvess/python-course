import contas
import cliente


class Banco:
    def __init__(
        self,
        agencias: list[int] | None = None,
        clientes: list[cliente.Pessoa] | None = None,
        contas: list[contas.Conta] | None = None,
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

    def autenticar(self, cliente: cliente.Pessoa, conta: contas.Conta):
        return self._checa_cliente(cliente) and self._checa_conta(conta) \
            and self._checa_agencia(conta)

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attr = f'Agências: {self.agencias}, Clientes: {self.clientes}, '\
            f'Contas: {self.contas}'
        return f'{class_name}({attr})'


if __name__ == '__main__':
    cliente1 = cliente.Pessoa('João', 18)
    conta_corrente1 = contas.ContaCorrente(111, 456, 1000, 1000)
    cliente1.conta = conta_corrente1

    banco1 = Banco()
    banco1.clientes.extend([cliente1])
    banco1.contas.extend([conta_corrente1])
    banco1.agencias.extend([111])

    if banco1.autenticar(cliente1, conta_corrente1):
        cliente1.conta.depositar(500)
        cliente1.conta.sacar(200)
