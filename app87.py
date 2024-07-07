class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f'Hello, {self.name}!', self.__class__.__name__)


class Client(Person):
    ...


c1 = Client('Alice')
c1.say_hello()  # Hello, Alice!
