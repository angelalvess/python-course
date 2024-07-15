from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int


p1 = Person('Luiz', 32)
print(p1)
