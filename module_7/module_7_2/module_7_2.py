def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'w', encoding='UTF-8')
    for num, string in enumerate(strings):
        strings_positions[(num, file.tell())] = string
        file.write(string + '\n')
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
