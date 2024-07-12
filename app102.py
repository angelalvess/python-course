from datetime import date


class Person:

    def __init__(self, name, birth):
        self.name = name
        self.birth = birth

    def lived_days(self):
        return (date.today() - self.birth).days

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError('name must be a string')
        self.__name = value

    @property
    def birth(self):
        return self.__birth

    @birth.setter
    def birth(self, value):
        if not isinstance(value, date):
            raise ValueError('birth must be a date object')
        self.__birth = value


p1 = Person('Alice', date(1990, 1, 1))
print(p1)
print(p1.lived_days())
