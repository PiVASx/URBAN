def print_params(a=1, b='строка', c=True):
    return a, b, c


print(print_params(a=25))
print(print_params(c=[1, 2, 3]))  # Немного не коррект т.к. мы к бул ставим массив лучше так не делать
print(print_params())
print()

values_list = ['str', True, 555]
values_dict = {'a': 2, 'b': 'удача', 'c': False}

print(print_params(*values_list))
print(print_params(**values_dict))
print()

values_list_2 = [88888, 'Строка']
print(print_params(*values_list_2, False))
print()

def append_to_list(item, list_my=None):
    if list_my is None:
        list_my = []
    list_my.append(item)
    return list_my


print(append_to_list('В листе'))
print(append_to_list('В листе 2'))
