from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__(name=name)  # Передаем имя потока в родительский класс, служит именем потока
        self.name = name
        self.power = power
        self.war_nps = 100
        self.fait_day = 0

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.war_nps > 0:
            sleep(0.1)
            self.war_nps -= self.power
            self.fait_day += 1
            print(f"{self.name} сражается {self.fait_day}..., осталось {self.war_nps} воинов.")

        print(f"{self.name} одержал победу спустя {self.fait_day} дней(дня)!")


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
# Вывод строки об окончании сражения
first_knight.join()
second_knight.join()
