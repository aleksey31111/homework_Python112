### Term 1 ###
print("Задание: Создать Класс Pair:\n"
      "\t1) Свойства Класса Pair:\n"
      "\t\t1.a - Числа A и B;\n"
      "\t2) Методы Класса Pair:\n"
      "\t\t2.a - Изменение Чисел;\n"
      "\t\t2.b - Вычисление Их Произведенмя и Суммы;\n"
      "Определить Произволный Класс Right_Triangle\n"
      "\t1) Свойства Производного Класса Right_Triangle:\n"
      "\t\t1.a - Катеты A и B;\n"
      "\t2) Методы Производного Класса Right_Triangle:\n"
      "\t\t2.a - Вычисление Гипотенузы и Площади Треугольника;\n"
      "\t\t2.b - Вывод Информации о Фигуре на Экран;\n"
      "Продемонстрировать Работу Класса-Наследника и всех Его Методов.")
print()

from math import sqrt


class Pair:
    def __init__(self, A, B):
        self.__a = A
        self.__b = B

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, A):
        self.__a = A

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, B):
        self.__b = B

    def sum_A_B(self):
        return self.a + self.b

    def multiply_A_B(self):
        return self.a * self.b


class Right_Triangle(Pair):
    def __init__(self, A, B):
        super().__init__(A, B)

    def hypotenuse_Right_Triangle(self):
        return round(sqrt(pow(self.a, 2) + pow(self.b, 2)), 2)

    def square_Right_Triangle(self):
        return 0.5 * self.a * self.b

    def info_Right_Triangle(self):
        print(f"Гипотенуза ABC: {self.hypotenuse_Right_Triangle()}\n"
              f"Прямоугольный треугольник ABC ({self.a, self.b, self.hypotenuse_Right_Triangle()})\n"
              f"Площадь ABC: {self.square_Right_Triangle()}")


right_triangle = Right_Triangle(5, 8)
right_triangle.info_Right_Triangle()
print()
print(f"Сумма: {right_triangle.sum_A_B()}")
print(f"Произведение: {right_triangle.multiply_A_B()}")
print()
right_triangle.a = 11
right_triangle.b = 3
print(f"Гипотенуза ABC: {right_triangle.hypotenuse_Right_Triangle()}")
right_triangle.a = 11
right_triangle.b = 22
print(f"Гипотенуза ABC: {right_triangle.hypotenuse_Right_Triangle()}")
print(f"Сумма: {right_triangle.sum_A_B()}")
print(f"Произведение: {right_triangle.multiply_A_B()}")
print(f"Площадь ABC: {right_triangle.square_Right_Triangle()}")
