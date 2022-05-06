### task 1 ##
print("Задание 1: Класс <Треугольник>, Дескриптор - Ввод сторон <int > 0>\n"
      "\t\t   Проверка На существование Треугольника.")
print()


class WholePositiveExistsTriangle:
    @classmethod
    def verify_whole_number_of_side(cls, side):
        if not isinstance(side, int):
            raise TypeError(f"Сторона Треугольника {side} должна быть целым числом")

    @classmethod
    def verify_positive_side(cls, side):
        if side < 0:
            raise ValueError(f"Сторона Треугольника {side} должна быть положительным числом")

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        # getattr(instance, self.name)
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.verify_whole_number_of_side(value)
        self.verify_positive_side(value)
        # setattr(instance, self.name, value)
        instance.__dict__[self.name] = value


class Triangle:
    ab = WholePositiveExistsTriangle()
    bc = WholePositiveExistsTriangle()
    ca = WholePositiveExistsTriangle()

    def __init__(self, ab, bc, ca):
        self.ab = ab
        self.bc = bc
        self.ca = ca

    def triangle_exists(self):
        if self.ab + self.bc < self.ca or self.bc + self.ca < self.ab or self.ca + self.ab < self.bc:
            return True
        else:
            return False

    def info(self):
        if self.triangle_exists():
            return f"Треугольника со сторонами {self.ab, self.bc, self.ca} не существкет."
        else:
            return f"Треугольник cо сторонами {self.ab, self.bc, self.ca} существует."


t1 = Triangle(2, 5, 6)
print(t1.info())
t2 = Triangle(5, 2, 8)
print(t2.info())
t3 = Triangle(7, 3, 6)
print(t3.info())
