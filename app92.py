class Ponto:
    def __init__(self, x, y, z='testing'):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}({self.x!r}, {self.y!r}, {self.z!r})'


p1 = Ponto(1, 2)
p2 = Ponto(3, 4)

print(p1)
print(p2)
