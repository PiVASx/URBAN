data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum_no_recurs(lst_):
    # Переведем массив в строку
    str_ = ' '.join(map(str, lst_))
    # Удаляем все лишние символы оставляем только буквы и цифры и пробелы, преобразуем в лист по пробелам
    lst_ = ''.join(i for i in str_ if i.isalnum() or i in ' ').split(' ')
    # Считаем сумму проверя каждый элемент на число
    summ = 0
    for x in lst_:
        if x.isdigit():
            summ += int(x)
        else:
            summ += len(x)
    return summ


result = calculate_structure_sum_no_recurs(data_structure)
print(f'Решение без рекурсии: {result}')


def calculate_structure_sum(data_structure):
    summ = 0
    if isinstance(data_structure, str):
        summ += len(data_structure)
    elif isinstance(data_structure, (int, float)):
        summ += data_structure
    elif isinstance(data_structure, (list, set, tuple)):
        for x in data_structure:
            summ += calculate_structure_sum(x)
    elif isinstance(data_structure, dict):
        for x, y in data_structure.items():
            summ += calculate_structure_sum(x)
            summ += calculate_structure_sum(y)
    return summ


result = calculate_structure_sum(data_structure)
print(f'Решение через рекурсию: {result}')
