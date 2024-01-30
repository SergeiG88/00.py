import time
from threading import Thread
import threading
import queue


class Table:
    def __init__(self, number):
        # super().__init__(*args, **kwargs)
        self.number = number
        self.is_busy = False
        # self.catcher = queue.Queue(maxsize=2)


class Customer(threading.Thread):
    def __init__(self, number, cafe):
        super().__init__()
        self.cafe = cafe
        self.number = number

    def run(self, table):
        table - self.cafe.get_free_table()
        if table:
            print(f'Посетитель номер {self.number} сел за стол {table.number}')
            time.sleep(5)
            # table.is_busy = True
            print(f'Посетитель номер {self.number} покушал и ушел')
        else:
            print(f'Посетитель номер {self.number} ожидает свободный стол')


class Cafe:
    def __init__(self, tables):
        self.q = queue.Queue()

        # self.queue = []
        self.tables = tables

    def get_free_table(self):
        for table in self.tables:
            if not table.is_busy:
                table.is_busy == True
                return table



customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

customer_arrival_thread.join()