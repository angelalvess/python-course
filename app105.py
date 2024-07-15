from dataclasses import dataclass


@dataclass
class Person:
    name: str
    surname: str

    def complete_name(self):
        return f'{self.name} {self.surname}'


p1 = Person('Angie', 'Alves')

print(p1)
print(p1.complete_name())
