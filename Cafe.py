import time
import threading
import queue


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Customer(threading.Thread):
    def __init__(self, number, cafe):
        super().__init__()
        self.cafe = cafe
        self.number = number
        self.table = None

    def take_table(self, free_table):
        self.table = free_table
        free_table.is_busy = True

    def leave_table(self, free_table):
        self.table = None
        free_table.is_busy = False

    def run(self):
        self.cafe.serve_customer()


class Cafe:
    def __init__(self, tables):
        self.q = queue.Queue()
        self.tables = tables
        self.locker = threading.Lock()

    def check_table(self):
        for table in self.tables:
            if not table.is_busy:
                return table
        return False

    def customer_arrival(self):
        for customer_number in range(1,21):
            customer = Customer(customer_number, self)
            with self.locker:

                print(f'Посетитель номер {customer_number} прибыл')
                if not self.check_table():
                    print(f'Посетитель номер {customer.number} ожидает свободный стол')
                    time.sleep(1)
            customer.start()
            self.q.put(customer)


    def serve_customer(self):
        free_table = self.check_table()

        while not self.q.empty() and free_table:
            cur_customer = self.q.get()
            with self.locker:
                print(f'Посетитель номер {cur_customer.number} сел за стол {free_table.number}')
                cur_customer.take_table(free_table)
                time.sleep(1)
            time.sleep(4)
            with self.locker:
                print(f'Посетитель номер {cur_customer.number} покушал и ушел')
                cur_customer.leave_table(free_table)
                time.sleep(1)
                free_table = self.check_table()





table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]
cafe = Cafe(tables)

customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)

customer_arrival_thread.start()

customer_arrival_thread.join()
