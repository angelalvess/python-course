class Caneta:
    def __init__(self, cor):
        self._cor = cor

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, value):
        self._cor = value


caneta = Caneta('azul')
caneta.cor = 'vermelha'
print(caneta.cor)
