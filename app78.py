import json

PATH_FILE = 'app78_a.py'


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)
p2 = Person("Mari", 20)
p3 = Person("Angel", 16)
bd = [p1.__dict__, p2.__dict__, p3.__dict__]


def fazer_dumpo():
    with open(PATH_FILE, 'w', encoding='utf-8') as file:
        json.dump(bd, file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    fazer_dumpo()
    print('Done!')
