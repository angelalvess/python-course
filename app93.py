class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}({self.x!r}, {self.y!r})'

    def __add__(self, other):
        other_x = self.x + other.x
        other_y = self.y + other.y
        return Ponto(other_x, other_y)

    def __gt__(self, other):
        result_self = self.x + self.y
        result_other = other.x + other.y
        return result_self > result_other


p1 = Ponto(1, 2)
p2 = Ponto(3, 4)
p3 = p1 + p2
print(p3)
print('p1 é maior que p2: ', p1 > p2)
print('p2 é maior que p1: ', p2 > p1)
