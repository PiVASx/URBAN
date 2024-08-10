grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Переводим в массив и сортируем
students = sorted(list(students))
# Получаем среднее значение
grades = list(map(lambda x: sum(x) / len(x), grades))
# Собираем через zip и выводим на экран
print(dict(zip(students, grades)))
