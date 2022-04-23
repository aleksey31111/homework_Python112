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
    def __init__(self, a, b, c=None):
        if c is None:
            self.a = a
            self.b = b
        self.a = a
        self.b = b
        self.c = c

    @abstractmethod
    def root_quadratic_equation(self):
        pass

    @abstractmethod
    def root_linear_equation(self):
        pass

    def print_root_linear_equation(self):
        return -self.b / self.a

    def print_root_quadratic_equation(self):
        print((-self.b + sqrt(self.b ** 2 - 4 * self.a * self.c) / 2 * self.a),
              (-self.b + sqrt(self.b ** 2 - 4 * self.a * self.c)) / 2 * self.a)


class Linear(Root):  # 3x +7 = 0
    def __init__(self, a, b):
        super().__init__(self.a, self.b)

    def root_linear_equation(self):
        super().root_linear_equation()
        return -self.b / self.a

    def print_root_linear_equation(self):
        super().print_root_linear_equation()
        print(f"The root of '3x+7=0' is {-self.b / self.a}")


class Quadratic(Root):  # x^2 - 2x - 3 = 0
    def __init__(self, a, b, c):
        super().__init__(a, b, c)  # (-b + sqrt(d))/2a

    #     self.d = d  # b^2 - 4ac
    #     super(Quadratic, self).__init__(root1)  # (-b + sqrt(d))/2a
    #     self.root2 = root2  # (-b - sqrt(d))/2a

    def root_quadratic_equation(self):
        super().root_quadratic_equation()
        d = pow(self.b, 2) - 4 * 1 * 3
        root1 = (-self.b + sqrt(d)) / 2 * self.a
        root2 = (-self.b - sqrt(d)) / 2 * self.a
        return root1, root2

    def print_root_quadratic_equation(self):
        super().print_root_quadratic_equation()

        print(f"The roots of '1x^2-2x-3=0' is: {Quadratic.root_quadratic_equation()}")


r = Root
l = Linear
q = Quadratic
# l(3, 7)
# q(1, -2, -3)
