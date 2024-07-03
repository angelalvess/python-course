class Camera:
    def __init__(self, name, filmando=False):
        self.name = name
        self.filmando = filmando

    def filmar(self):

        if self.filmando:
            print(f'{self.name} is already filming')
            return

        print(f'{self.name} is filming')
        self.filmando = True

    def parar(self):
        print(f'{self.name} stopped filming')
        self.filmando = False


c1 = Camera('Canon')
c2 = Camera('Nikon')

c1.filmar()
c1.filmar()

print(c1.filmando)
print(c2.filmando)

c1.parar()
print(c1.filmando)
