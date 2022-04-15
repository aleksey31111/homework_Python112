from math import sqrt

### Term 1 ###
print("Задание: Создать класс Вычисляющий Площади разных Фигур.\n"
      "Функциональность Класса Подсчет: 1 - Площади Треугольника по разным Формулам.\n"
      "2 - Площади Прямоугольника. 3 - Площади Квадрата.\n"
      "Методы Класса, Подсчета Площади Реализованны Статическими Методами Класса.\n"
      "Возвращать Количество Подсчетов Площади.")


class Figures_square:
    count = 0

    def __init__(self, triangle_a, triangle_b, triangle_c,
                 triangle_base, triangle_height, rectangle_a, rectangle_b):
        self.triangle_a = triangle_a
        self.triangle_b = triangle_b
        self.triangle_c = triangle_c
        self.triangle_base = triangle_base
        self.triangle_height = triangle_height
        self.rectangle_a = rectangle_a
        self.rectangle_b = rectangle_b

    @staticmethod
    def geron_square(triangle_a, triangle_b, triangle_c):
        p = 0.5 * (triangle_a + triangle_b + triangle_c)
        print(f"Площадь треугольника по формуле Герона ({triangle_a, triangle_b, triangle_c}): "
              f"{sqrt(p * (p - triangle_a) * (p - triangle_b) * (p - triangle_c))}")
        Figures_square.count += 1

    @staticmethod
    def base_height_square(triangle_base, triangle_height):
        print(f"Площадь треугольника через основание и высоту ({triangle_base, triangle_height}): "
              f"{0.5 * triangle_base * triangle_height}")
        Figures_square.count += 1

    @staticmethod
    def square_square(square_a):
        print(f"Площадь квадрата ({square_a}): "
              f"{pow(square_a, 2)}")
        Figures_square.count += 1

    @staticmethod
    def rectangle_square(rectangle_a, rectangle_b):
        print(f"Площадь прямоугольника ({rectangle_a, rectangle_b}): "
              f"{rectangle_b * rectangle_a * 0.5}")
        Figures_square.count += 1


Figures_square.geron_square(3, 4, 5)
Figures_square.base_height_square(6, 7)
Figures_square.square_square(7)
Figures_square.rectangle_square(2, 6)
print(f"Количество подсчетов площади: {Figures_square.count}")
