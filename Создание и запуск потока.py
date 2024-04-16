import threading
import time


def number():
    for i in range(1,11):
        print(i)
        time.sleep(1)


def num():
    for num in 'abcdefghij':
        print(num)
        time.sleep(1)


t1 = threading.Thread(target=number)
t2 = threading.Thread(target=num)


t1.start()
t2.start()

t1.join()
t2.join()












