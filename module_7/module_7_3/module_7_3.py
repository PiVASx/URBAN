from pprint import pprint
class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = [x for x in file_names]

    def get_all_words(self):
        all_words = {}

        for num, file_path in enumerate(self.file_names):
            with open(file_path, encoding='utf-8') as file:
                punctuation = ".,=!?:; -"
                # Считываем из файла и переводим в нижний регистр
                texts = file.read().lower()
                # Сплитим строку по пробелам, после каждый символ проверяем на пунктуацию
                text = [''.join(char for char in text if char not in punctuation) for text in texts.split()]
                # Получаем имя файла если оно находится во вложении
                if file_path.rfind('/') != -1:
                    file_name = file_path[file_path.rfind('/')+1:]
                    all_words[file_name] = text
                else:
                    all_words[file_path] = text
        return all_words

    def find(self, word):
        all_words = {}

        for key, value in self.get_all_words().items():
            for i, v in enumerate(value):
                if v == word.lower():
                    all_words[key] = i+1
                    break

        return all_words

    def count(self, word):
        count = 0
        all_words = {}

        for key, value in self.get_all_words().items():
            for i, v in enumerate(value):
                if v == word.lower():
                    count += 1

            all_words[key] = count
            count = 0

        return all_words


# Передаем 1 файл
finder1 = WordsFinder('test_file.txt')
print(finder1.get_all_words())  # Все слова
print(finder1.find('TEXT'))  # 3 слово по счёту
print(finder1.count('teXT'))  # 4 слова teXT в тексте всего
print()

# Передаем 2 файл
finder2 = WordsFinder('Mother Goose - Monday’s Child/Mother Goose - Monday’s Child.txt')
print(finder2.get_all_words())
print(finder2.find('Child'))
print(finder2.count('Child'))
print()

# Передаем 3 файл
finder3 = WordsFinder('Walt Whitman - O Captain! My Captain!/Walt Whitman - O Captain! My Captain!.txt')
print(finder3.get_all_words())
print(finder3.find('captain'))
print(finder3.count('captain'))
print()

# Передаем All файл
finderAll = WordsFinder('All/Mother Goose - Monday’s Child.txt',
                        'All/Rudyard Kipling - If.txt',
                        'All/Walt Whitman - O Captain! My Captain!.txt')
print(finderAll.get_all_words())
print(finderAll.find('the'))
print(finderAll.count('the'))

