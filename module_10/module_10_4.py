from random import randint
from threading import Thread, Lock
from time import sleep


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 11))


class Cafe:
    pass
