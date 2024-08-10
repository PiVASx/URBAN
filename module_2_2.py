inp = set(map(int, input('Введите 3 числа: ').split(' ')))
print(inp)
if len(inp) == 3:
    print(0)
elif len(inp) == 2:
    print(2)
elif len(inp) == 1:
    print(3)
else:
    print('Введенные числа не попали ни под одно условие.')
