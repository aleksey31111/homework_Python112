from abc import ABC, abstractmethod

### Task 1 ###
print("Задание 1:\n"
      "\t1) Создать Базовый Абстракный Класс \"Корень\":\n"
      "\t\t1.a - Методы Вычисления Корней Уравнения;\n"
      "\t\t1.b - Вывод Результата На Экран;\n"
      "\t2) Реализовать Производные Классы \"Линейное Уравнение\" и \"Квадратное Уравнение\":\n"
      "\t\t2.a - Методы Вычисления Корней;\n"
      "\t\t2.b - Вывод Результатов на Экран;")


class Root:
    def __init__(self, root):
        self.root = root

    @abstractmethod
    def root_quadratic_equation(self):
        pass

    @abstractmethod()
    def root_linear_equation(self):
        pass

    def print_roots(self):
        print(self.root)


class Linear:
    def __init__(self, x):
        self.x = x

    def root_linear_equation(self):

