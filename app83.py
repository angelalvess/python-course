class Escritor:
    def __init__(self, name):
        self.name = name
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, value):
        self._ferramenta = value


class FerramentaDeEscrever:
    def __init__(self, name):
        self.name = name

    def escrever(self):
        return f'{self.name} está escrevendo...'


escritor = Escritor('João')
caneta = FerramentaDeEscrever('Caneta')
escritor.ferramenta = caneta

print(caneta.escrever())
print(escritor.ferramenta.escrever())
