def gen1():

    yield 1
    yield 2
    yield 3


def gen2():
    yield from gen1()
    yield 4
    yield 5


gen = gen2()

for n in gen:
    print(n)
