from random import randint
from threading import Thread, Lock
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        i = 0
        while i < 100:
            num = randint(50, 501)
            if self.lock.locked() and self.balance >= 500:
                self.lock.release()  # Освобождаем блокировку, если баланс >= 500

            self.lock.acquire()  # Пытаемся захватить блокировку
            try:
                self.balance += num
                print(f"Пополнение: {num}. Баланс: {self.balance}")
            finally:
                self.lock.release()  # Освобождаем блокировку
            i += 1
            time.sleep(0.001)

    def take(self):
        i = 0
        while i < 100:
            num = randint(50, 501)
            print(f'Запрос на {num}')
            self.lock.acquire()  # Пытаемся захватить блокировку
            try:
                if num <= self.balance:
                    self.balance -= num
                    print(f"Снятие: {num}. Баланс: {self.balance}")
                else:
                    print(f'Запрос отклонён, недостаточно средств.')
            finally:
                self.lock.release()  # Освобождаем блокировку
            i += 1
            time.sleep(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
