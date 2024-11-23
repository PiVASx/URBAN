import pandas as pd  # Таблицы
import matplotlib.pyplot as plt  # Отрисовка графиков
import numpy as np  # Numpy

# Считываем файл с данными с помощью pandas создаем таблицу
df = pd.read_csv('18_19.csv', sep=';')
print(df.head(5))  # Выводим 5 первых строк таблицы
print()
print(df.shape)  # Размер базы количество строк и столбцов

# Редактируем таблицу
# Сместим CLOSE на последний индекс
df['new_CLOSE'] = df['CLOSE']  # копируем CLOSE и добавляем в конец
df = df.drop(['DATE', 'TIME', 'CLOSE'], axis=1)  # Удаляем ненужные столбцы
df.rename(columns={'new_CLOSE': 'CLOSE'}, inplace=True)  # Переименовываем столбец new_CLOSE
print('\nРезультат редактирования.\n')
print(df.head(5))  # Выводим 5 первых строк таблицы
print()
print(df.shape)  # Размер базы количество строк и столбцов
print()

# Визуализируем таблицу.
data = np.array(df)  # Превращаем pandas в numpy массив

# Отображаем часть данных с базы ввиде графика
start = 10000  # С какой точки начинаем
length = 300  # Сколько точек отрисуем
chanelNames = ['OPEN', 'MAX', 'MIN', 'CLOSE']

# Рисуем все график
plt.figure(figsize=(22, 6))  # Создаем полотно для графика
for i in chanelNames:  # Проходимся по массиву для фильтрование нужных колонок
    if i in df.columns:  # Если совпадает добавляем график
        x = df.columns.get_loc(i)  # Узнаем индекс столбца
        plt.plot(data[start:start + length, x], label=df.columns[
            x])  # От начальной точки, до начальной точки + размер шага отрисовки лейбел бирется с базы по индексу
plt.ylabel('Цена.руб')  # Добавляем название У
plt.xlabel('Час')  # Добавляем название У
plt.legend()  # Отобразить легенды на полотне
plt.show()  # Показать график
