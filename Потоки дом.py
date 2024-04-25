from threading import Thread
import threading

class BankAccount(threading.Thread):
    def __init__(self, amount):
        threading.Thread.__init__(self)
        self.amount = amount
        self.balance = 1000
        self.balance_lock = lock

    def deposit_task(self, amount):
        for _ in range(5):
            with lock:
                self.balance += amount
                print(f'Deposited {amount}, new balance is {self.balance}')


    def withdraw_task(self, amount):
        for _ in range(5):
            with lock:
                self.balance -= amount
                print(f'Withdrew  {amount}, new balance is {self.balance}')

lock = threading.Lock()
account = BankAccount(1000)

deposit_thread = threading.Thread(target=BankAccount.deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=BankAccount.withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
