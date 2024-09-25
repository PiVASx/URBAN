def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        return str(a) + str(b)
    finally:
        print('Расчет окончен!!!')


print(add_everything_up(5, 5))
print(add_everything_up(5, 'qwer'))
print(add_everything_up('qwe', 5))
