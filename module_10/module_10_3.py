from threading import Thread, Lock
import time

class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.lock = Lock()

    def deposit(self):
        num = range(50, 501)
        if self.balance >= 500 and self.lock.locked():
            self.lock.release()
        self.balance += num
        print(f"Пополнение: {num}. Баланс: {self.balance}")
        time.sleep(0.001)

