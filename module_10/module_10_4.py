from msilib.schema import tables
from random import randint
from threading import Thread, Lock
from time import sleep
from queue import Queue

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


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

    def guest_arrival(self, *guests):
        for guest in guests:
            # Проверяем наличие свободного стола
            for table in self.tables:
                if table.guest is None:  # Если стол свободен
                    table.guest = guest  # Сажаем гостя за стол
                    guest.start()  # Запускаем поток гостя
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    break
            else:
                # Если все столы заняты, помещаем в очередь
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None:  # Если за столом есть гость
                    if not table.guest.is_alive():  # Если гость закончил приём пищи
                        print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                        print(f"Стол номер {table.number} свободен")
                        table.guest = None  # Освобождаем стол

                        # Если очередь не пуста, сажаем следующего гостя
                        if not self.queue.empty():
                            next_guest = self.queue.get()
                            table.guest = next_guest
                            next_guest.start()  # Запускаем поток следующего гостя
                            print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
            sleep(1)



# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()