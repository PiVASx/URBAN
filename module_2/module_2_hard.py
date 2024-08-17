def pairs_numbers(num):
    pairs = []
    for i in range(1, num):
        for j in range(1, 20):
            if i < j and num % (i + j) == 0:
                pairs.append(i)
                pairs.append(j)
    return ''.join(str(x) for x in pairs)


print(f'Для 3 - {pairs_numbers(3)}')
print(f'Для 4 - {pairs_numbers(4)}')
print(f'Для 5 - {pairs_numbers(5)}')
print(f'Для 6 - {pairs_numbers(6)}')
print(f'Для 7 - {pairs_numbers(7)}')
print(f'Для 8 - {pairs_numbers(8)}')
print(f'Для 9 - {pairs_numbers(9)}')
print(f'Для 10 - {pairs_numbers(10)}')
