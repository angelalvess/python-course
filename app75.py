class Person:
    def __init__(self, name):
        self.name = name

    def eating(self, food):
        return f'{self.name} is eating {food}'


p1 = Person('Angel')

print(p1.eating('sushi'))
