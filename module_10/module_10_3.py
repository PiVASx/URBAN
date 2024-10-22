

class Bank:
    def __init__(self, balance, lock):
        self.balance = balance
        self.lock = lock

    def deposit(self, num):
        if 50 >= num <= 500:
            self.balance += num


