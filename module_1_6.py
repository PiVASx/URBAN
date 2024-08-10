my_dict = {'Максим': 1944, 'Ли': 1988, 'Артур': 1997}
print(f'Dict: {my_dict}')
print(f'Existing value: {my_dict.get('Ли')}\nNot existing value: {my_dict.get('Василий')}')
my_dict.update({'Василий': 1977, 'Николай': 2000})
print(f'Deleted value: {my_dict.pop('Василий')}')
print(f'Modified dictionary: {my_dict}\n')

my_set = {1, True, 'STR', 1}
print(f'Set: {my_set}')
my_set.update([False, 4])
my_set.remove(False)
print(f'Modified set: {my_set}')