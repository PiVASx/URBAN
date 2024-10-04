first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']


first_result = (len(x) - len(z) for x, z in zip(first, second) if len(x) != len(z))

second_result = (len(first[index]) == len(second[index]) for index in range(len(first)))

print(list(first_result))
print(list(second_result))