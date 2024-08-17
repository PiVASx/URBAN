immutable_var = 1, True, [1, 2]
print(immutable_var)
# immutable_var[0] = 2 # Получим ошибку так как он является не изменяемым.

mutable_list = [1, 5, 2, True, [1, 2]]
mutable_list[-1] = 'Изменен'
print(mutable_list)
