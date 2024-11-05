from random import randint
from threading import Thread, Lock
from time import sleep
from queue import Queue


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
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, guest):
        self.queue.put(guest)
        print(f"Гость {guest} встал в очередь.")

    def discuss_guests(self):
        pass