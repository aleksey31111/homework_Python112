from abc import ABC, abstractmethod
from math import sqrt
### Task 1 ###
print("Задание 1:\n"
      "\t1) Создать Базовый Абстракный Класс \"Корень\":\n"
      "\t\t1.a - Методы Вычисления Корней Уравнения;\n"
      "\t\t1.b - Вывод Результата На Экран;\n"
      "\t2) Реализовать Производные Классы \"Линейное Уравнение\" и \"Квадратное Уравнение\":\n"
      "\t\t2.a - Методы Вычисления Корней;\n"
      "\t\t2.b - Вывод Результатов на Экран;")


class Root(ABC):
    def __init__(self, root1, root2=None, d=None):
        if root2 is None or d is None:
            self.root1 = root1
        self.root1 = root1
        self.root2 = root2

    @abstractmethod
    def root_quadratic_equation(self):
        pass

    @abstractmethod
    def root_linear_equation(self):
        pass

    def print_root_linear_equation(self):
        print(self.root1)

    def print_root_quadratic_equation(self):
        print(self.root1, self.root2)


class Linear(Root):
    # def __init__(self, root1):
    #     super(Linear, self).__init__(root1)

    def root_linear_equation(self):

        self.root1 = -7 / 3
        return self.root1

    def print_root_linear_equation(self):
        super().print_root_linear_equation()
        print(f"The root of '3x+7=0' is {self.root1}")


class Quadratic(Root):  # x^2 - 2x - 3 = 0
    # def __init__(self, d, root1, root2):
    #     self.d = d  # b^2 - 4ac
    #     super(Quadratic, self).__init__(root1)  # (-b + sqrt(d))/2a
    #     self.root2 = root2  # (-b - sqrt(d))/2a

    def root_quadratic_equation(self):
        self.d = pow(2, 2) - 4 * 1 * 3
        self.root1 = (-2 + sqrt(self.d)) / 2 * 1
        self.root2 = (-2 - sqrt(self.d)) / 2 * 1
        return self.root1, self.root2

    def print_root_quadratic_equation(self):
        print(f"The roots of '1x^2-2x-3=0' is: {self.root1}, {self.root2}")


R = Root()
# rle = Linear()