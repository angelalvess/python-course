class Person:

    year = 2024

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def greet(cls):
        print('Hello!')

    @classmethod
    def cria_sem_nome(cls, age):
        return cls('Anônimo', age)


p1 = Person("John", 36)
p2 = Person.cria_sem_nome(20)
print(Person.year)
print(p2.name, p2.age)
Person.greet()
