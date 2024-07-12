class CallMe:

    def __init__(self, phone):
        self.phone = phone

    def __call__(self):
        print(f'Calling {self.phone}...')


call1 = CallMe('123-456-7890')
call1()
