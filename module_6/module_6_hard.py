import math


class Figure:
    sides_count = 0

    def __init__(self, color, sides, filled=False):
        self.__sides = [sides for _ in range(sides)]
        self.filled = filled
        if Figure.__is_valid_color(color):
            self.__color = list(color)
        else:
            self.__color = [255, 255, 255]

    @staticmethod
    def __is_valid_color(color):
        return (isinstance(color, (tuple, list)) and len(color) == 3
                and all(isinstance(x, int) and 0 <= x <= 255 for x in color))

    def __is_valid_sides(self, sides):
        return all(x > 0 for x in sides) and len(sides) == self.sides_count

    def get_color(self):
        return self.__color

    def set_color(self, *color):
        if Figure.__is_valid_color(color):
            self.__color = list(color)

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        """
        Периметр/длина фигуры.
        Если фигура — это круг, возвращает длину окружности (периметр круга).
        В остальных случаях возвращает сумму сторон (периметр).
        """
        if isinstance(self, Circle):
            return 2 * math.pi * self.get_radius()
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__radius = sides / 2

    def get_radius(self):
        return self.__radius

    def get_square(self):
        return math.pi * self.get_radius() ** 2


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        p = sum(self.__sides) / 2
        a, b, c = self.__sides
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


class Cube(Figure):
    sides_count = 12


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
# print(cube1.get_volume())
