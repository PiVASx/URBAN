from threading import Thread
from time import sleep
from datetime import datetime


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for x in range(1, word_count + 1):
            file.write(f'Какое-то слово № {x}\n')
            sleep(0.1)


stat = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
print(f'Время затраченное на не асинхронную обработку {datetime.now() - stat}')

stat = datetime.now()
p1 = Thread(target=write_words, args=(10, 'example5.txt'))
p2 = Thread(target=write_words, args=(30, 'example6.txt'))
p3 = Thread(target=write_words, args=(200, 'example7.txt'))
p4 = Thread(target=write_words, args=(100, 'example8.txt'))

p1.start()
p2.start()
p3.start()
p4.start()

p1.join()
p2.join()
p3.join()
p4.join()
print(f'Время затраченное на асинхронную обработку {datetime.now() - stat}')
