def my_planet(method_):

    def inner(self, *args, **kwargs):
        result = method_(self, *args, **kwargs)

        if "Earth" in result:
            return "I'm from Earth"
        return result
    return inner


class Planet:
    def __init__(self, name):
        self.name = name

    @my_planet
    def say_planet(self):
        return self.name


earth = Planet('Earth')
mars = Planet('Mars')

print(earth.say_planet())
print(mars.say_planet())
