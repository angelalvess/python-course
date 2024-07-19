from collections.abc import Sequence


class MyList(Sequence):
    def __init__(self):
        self._data = {}
        self._index = 0

    def append(self, value):
        self._data[self._index] = value
        self._index += 1
        self._next = 0

    def __len__(self):
        return self._index

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __iter__(self):
        return self

    def __next__(self):
        if self._next >= self._index:
            raise StopIteration
        value = self._data[self._next]
        self._next += 1
        return value


if __name__ == '__main__':
    my_list = MyList()
    my_list.append('Angel')
    my_list.append('Maria')
    my_list.append('Lucas')
    my_list[2] = 'Angelina'
    # print(my_list[0])
    # print(len(my_list))

    for item in my_list:
        print(item)
