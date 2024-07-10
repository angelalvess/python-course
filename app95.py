from contextlib import contextmanager


@contextmanager
def my_open(filename, mode):

    try:
        print('open file')
        file = open(filename, mode, encoding='utf-8')
        yield file
    finally:
        print('close file')
        file.close()


with my_open('app95.txt', 'w') as file:
    file.write('Hello, World!', 123)
    print(file)
