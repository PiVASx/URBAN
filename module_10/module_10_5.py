import time
import multiprocessing

all_date_full = []
list_fname = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()  # Считываем строку
            if line == '':  # Проверяем, является ли строка пустой
                break  # Если строка пустая, выходим из цикла
            all_data.append(line)

    return all_data


"""print('Тест 1: Линейный запуск')

start_time = time.time()  # Запоминаем время начала выполнения
for x in list_fname:
    all_date_full.append(read_info(x))

print(len(all_date_full))
print(f"Время выполнения: {time.time() - start_time:.2f} секунд")"""


if __name__ == '__main__':
    print('Тест 2: Многопроцессорный запуск')
    start_time = time.time()  # Запоминаем время начала выполнения

    # Запуск многопроцессорность через Pool
    with multiprocessing.Pool() as pool:
        all_date_full = pool.map(read_info, list_fname)

    print(len(all_date_full))
    print(f"Время выполнения: {time.time() - start_time:.2f} секунд")
