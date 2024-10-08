class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        if self.valid_step(step):
            self.step = step
        self.start = start
        self.stop = stop
        self.pointer = 0

    def __iter__(self):
        # обнулим счетчик перед циклом
        self.pointer = self.start
        # возвращаем ссылку на себя, так как сам объект должен быть итератором
        return self

    def __next__(self):
        if self.step > 0:
            if self.pointer <= self.stop:
                # увеличивающий атрибут pointer на step
                result = self.pointer
                self.pointer += self.step
                return result
            else:
                raise StopIteration

        elif self.step < 0:
            if self.pointer >= self.stop:
                # увеличивающий атрибут pointer на step
                result = self.pointer
                self.pointer += self.step
                return result
            else:
                raise StopIteration

    @staticmethod
    def valid_step(step):
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')
        return True


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
    print()
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()
