def is_prime(func):
    def wrapper(*args):
        orig_result = func(*args)
        if orig_result <= 1:
            print("Составное")
        else:
            for i in range(2, int(orig_result ** 0.5) + 1):
                if orig_result % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        return orig_result

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


# Пример использования
result = sum_three(2, 3, 6)
print(result)
