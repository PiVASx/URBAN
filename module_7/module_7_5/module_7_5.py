import os
import time
directory = '.'
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        #print(filepath)
        filetime = os.stat(filepath).st_mtime
        #print(filetime)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        #print(formatted_time)
        file_size = os.stat(filepath).st_size
        #print(file_size)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, '
              f'Размер: {file_size} байт, Время изменения: {formatted_time}, '
              f'Родительская директория: {parent_dir}')