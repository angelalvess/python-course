class Carrinho:
    def __init__(self):
        self._produtos = []

    def adicionar_produto(self, *produtos):
        self._produtos.extend(produtos)

    def total(self):
        return sum([p.preco for p in self._produtos])

    def listar_produtos(self):
        for p in self._produtos:
            print(p.nome, p.preco)


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()
p1 = Produto('Camiseta', 50)
p2 = Produto('iPhone', 10000)
carrinho.adicionar_produto(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())
