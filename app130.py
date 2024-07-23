from time import sleep


from threading import Thread


class MyThread(Thread):

    def __init__(self, text, time):
        self.text = text
        self.time = time
        Thread.__init__(self)

    def run(self):
        sleep(self.time)
        print(self.text)


t1 = MyThread("Hello from thread 1", 5)
t1.start()

for i in range(10):
    print(i)
    sleep(1)
