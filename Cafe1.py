import time
from threading import Thread
import threading
import queue


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Customer(threading.Thread):
    def __init__(self, number, cafe, tables):
        super().__init__()
        self.cafe = cafe
        self.number = number
        self.tables = tables

    # def run(self, tables):
    #     tables = self.cafe.get_free_table()
    #     if tables:
    #         print(f'Посетитель номер {self.number} сел за стол {tables.number}')
    #         time.sleep(5)
    #         # table.is_busy = True
    #         print(f'Посетитель номер {self.number} покушал и ушел')
    #     else:
    #         print(f'Посетитель номер {self.number} ожидает свободный стол')


class Cafe:
    def __init__(self, tables):
        self.q = queue.Queue()
        self.tables = tables

    # def get_free_table(self):
    #     for table in self.tables:
    #         if not table.is_busy:
    #             table.is_busy == True
    #             return table

    def customer_arrival(self):
        # customer_number = 1
        for customer_number in range(1,21):
        # while customer_number <= 20:
            print(f'Посетитель номер {customer_number} пришел')
            # customer = Customer(customer_number, self)
            self.q.put(item=1)
            # time.sleep(1)
            # return
            # customer.start()


    def serve_customer(self):
        customer_tables = 1
        customer_number = 1

        while customer_tables <= 20:
                print(f'Посетитель номер {customer_tables} сел за стол N {customer_number}')
                print(f'Посетитель номер {customer_tables} покушал и ушел')
                # time.sleep(1)
                customer_tables += 1
                customer_number += 1
                # time.sleep(1)
        print(f'Посетитель номер {customer_tables} ожидает свободный стол N...')
        # return
        # time.sleep(5)


table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]
cafe = Cafe(tables)

customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
serve_customer_thread = threading.Thread(target=cafe.serve_customer)

customer_arrival_thread.start()
serve_customer_thread.start()

customer_arrival_thread.join()
serve_customer_thread.join()