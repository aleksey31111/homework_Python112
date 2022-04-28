### Term 1 ###
print("Задание: Класс Point3D (x, y, z)\n"
      "\t1 - Перегрузка Операторов Сложения, Вычитания, Умножения и Деления.\n"
      "\t2 - Сравнение Координат мужду собой И Запись/Считывание Значений через Ключи:\"x\",\"y\",\"z\"")


class Point3D:
    def __init__(self, x: int, y: int, z: int):
        if not isinstance(x, int) or not isinstance(y, int) or not isinstance(z, int):
            raise ValueError("Координаты Должны Быть Целым Числом")

        self.__x = x
        self.__y = y
        self.__z = z

    def get_format_coords(self):
        z = self.__z
        y = self.__y
        x = self.__x
        return f"{Point3D.__get_form(x)}, {Point3D.__get_form(y)}, {Point3D.__get_form(z)}"

    @staticmethod
    def __get_form(x):
        return str(x)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_z(self):
        return self.__z

    def __add__(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError("Правый Операнд Должен Быть Типом Point3D")

        return self.__x + other.__x, self.__y + other.__y, self.__z + other.__z

    def __sub__(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError("Правый Операнд Должен Быть Типом Point3D")

        return self.__x - other.__x, self.__y - other.__y, self.__z - other.__z

    def __mul__(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError("Правый Операнд Должен Быть Типом Point3D")

        return self.__x * other.__x, self.__y * other.__y, self.__z * other.__z

    def __truediv__(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError("Правый Операнд Должен Быть Типом Point3D")

        return self.__x / other.__x, self.__y / other.__y, self.__z / other.__z

    def __eq__(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError("Правый Операнд Должен Быть Типом Point3D")

        return self.__x == other.__x  # , self.__y == other.__y, self.__z == other.__z

p3d1 = Point3D(12, 15, 18)
p3d2 = Point3D(6, 3, 9)
print(f"Координаты 1-й точки: {p3d1.get_format_coords()}")
print(f"Координаты 2-й точки: {p3d2.get_format_coords()}")
sum_p3d = p3d1 + p3d2
print(f"Сложение координат: {sum_p3d}")
sub_p3d = p3d1 - p3d2
print(f"Вычитание координат: {sub_p3d}")
mul_p3d = p3d1 * p3d2
print(f"Умножение: {mul_p3d}")
truediv_p3d = p3d1 / p3d2
print(f"Умножение: {truediv_p3d}")
eq_p3d = p3d1 == p3d2
print(f"Равенство координат: {eq_p3d}")