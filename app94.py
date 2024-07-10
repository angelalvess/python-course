class MyOpen:

    def __init__(self, path_file, mode):
        self.path_file = path_file
        self.mode = mode
        self._file = None

    def __enter__(self):
        print('open file')
        self._file = open(self.path_file, self.mode, encoding='utf-8')
        return self._file

    def __exit__(self, class_exc, exc, exc_traceback):
        print('close file')
        self._file.close()

        raise class_exc(*exc.args).with_traceback(exc_traceback)


with MyOpen('app94.txt', 'w') as file:
    file.write('Hello, World!', 123)
    print(file)
