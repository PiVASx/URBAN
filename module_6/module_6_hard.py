class Figure:
    sides_count = 0

    def __init__(self, color, sides, filled):
        self.__sides = sides
        self.filled = filled
        if self.__is_valid_color(*color):
            self.__color = color
        else:
            self.__color = (255, 255, 255)
        self.__color = color

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):
        """
        Проверка валидности цвета.
        """
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= g <= 255:
                return True
        return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)


class Circle(Figure):
    sides_count = 1


class Triangle(Figure):
    sides_count = 3


class Cube(Figure):
    sides_count = 12
