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

    def run(self):
        self.cafe.serve_customer(self)


class Cafe:
    def __init__(self, tables):
        self.q = queue.Queue()
        self.tables = tables


    def customer_arrival(self):
        for customer_number in range(1,21):
            time.sleep(1)
            print(f'Посетитель номер {customer_number} прибыл')
            customer = Customer(customer_number, self)
            customer.start()


    def serve_customer(self, customer):
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f'Посетитель номер {customer.number} сел за стол {table.number}')
                time.sleep(3)
                print(f'Посетитель номер {customer.number} покушал и ушел')
                table.is_busy = False
                break
        else:
            print(f'Посетитель номер {customer.number} ожидает свободный стол')
            self.q.put(customer.number)

table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]
cafe = Cafe(tables)

customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)

customer_arrival_thread.start()

customer_arrival_thread.join()
