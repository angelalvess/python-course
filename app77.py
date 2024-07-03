class Person:
    actual_year = 2024

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_birth_year(self):
        return Person.actual_year - self.age


p1 = Person('John', 23)
p2 = Person('Jane', 25)

print(Person.actual_year)
print(p1.get_birth_year())
print(p2.get_birth_year())
