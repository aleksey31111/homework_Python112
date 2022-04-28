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
print()


class Root(ABC):
    def __init__(self, a, b, c=None):
        if c is None:
            self.a = a
            self.b = b
        else:
            self.a = a
            self.b = b
            self.c = c

    @abstractmethod
    def calc_root_equation(self):
        pass

    @abstractmethod
    def print_root_equation(self):
        # raise NotImplementedError("В дочернем классе должен быть определен Метод print_root_linear_equation()")
        pass

        # @abstractmethod
        # def print_root_quadratic_equation(self):
        raise NotImplementedError("В дочернем классе должен быть определен Метод print_root_quadratic_equation()")
        # pass
        pass

class Linear(Root):  # 3x +7 = 0
    def calc_root_equation(self):
        super().calc_root_equation()
        return -self.b / self.a

    def print_root_equation(self):
        print(f"The root of '3x+7=0' is {round(-self.b / self.a, 2)}")


class Quadratic(Root):  # x^2 - 2x - 3 = 0
    def calc_root_equation(self):
        super().calc_root_equation()
        d = self.b ** 2 - 4 * self.a * self.c
        root1 = (-self.b + sqrt(abs(d))) / 2 * self.a
        root2 = (-self.b - sqrt(abs(d))) / 2 * self.a
        return round(root1, 3), round(root2, 3)

    def print_root_equation(self):
        print(f"The roots of '1x^2-2x-3=0' is: {self.calc_root_equation()} ")


l = Linear(3, 7)
l.print_root_equation()
q = Quadratic(1, 2, 3)
q.print_root_equation()
