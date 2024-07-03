class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def speed(self):
        print(f'{self.make} is speeding up')


car1 = Car('Toyota', 'Corolla', 2019)
print(car1.make)
car1.speed()
print('------------------')

car2 = Car('Mazda', 'CX-5', 2020)
print(car2.make)
car2.speed()
