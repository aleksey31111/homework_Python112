class WholePositiveExistsTriangle:
    @classmethod
    def verify_positive_side(cls, side):
        if side < 0:
            raise ValueError(f"Сторона Треугольника {side} должна быть положительным числом")

    @classmethod
    def verify_whole_number_of_side(cls, side):
        if not isinstance(side, int):
            raise TypeError(f"Сторона Треугольника {side} должна быть целым числом")

    @classmethod
    def verify_exists_triangle(cls, ab, bc, ca):
        if ab + bc > ca or bc + ca > ab or ca + ab > bc:
            raise ValueError(f"Треугольника со сторонами {ab}, {bc}, {ca} Не Существкет.")

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        # getattr(instance, self.name)
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.verify_positive_side(value)
        self.verify_whole_number_of_side(value)
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

    def info(self):
        return f"Треугольник Со Сторонами {[self.ab, self.bc, self.ca]} Сущесьвует."


t1 = Triangle(2, 5, 6)
print(t1.info())
