class Carro:
    def __init__(self, name):
        self.name = name
        self.motor = None
        self.fabricante = None

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, value):
        self._fabricante = value

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, value):
        self._motor = value


class Motor:
    def __init__(self, name):
        self.name = name

    def ligar(self):
        return f'{self.name} está ligando...'


class Fabricante:
    def __init__(self, name):
        self.name = name

    def produzir(self):
        return f'{self.name} está produzindo...'


fusca = Carro('Fusca')

motor = Motor('Motor 123')
fusca.motor = motor

volkswagen = Fabricante('Volkswagen')
fusca.fabricante = volkswagen

print(fusca.motor.ligar())
print(fusca.fabricante.produzir())
