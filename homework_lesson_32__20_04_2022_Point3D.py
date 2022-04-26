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

    def get_format_coord(self):
        z = self.__z
        y = self.__y
        x = self.__x
        return f"{Point3D.__get_form(x)} : {Point3D.__get_form(y)} : {Point3D.__get_form(z)}"

    @staticmethod
    def __get_form(x):
        return str(x)

    def get_way(self):
        return self.__go

    def __add__(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError("Правый Операнд Должен Быть Типом Point3D")

        return self.__x + other.__x, self.__y + other.__y, self.__z + other.__z



p3d = Point3D(12, 1, 10)
p3d1 = Point3D(1, 12, 3)
print(p3d.get_format_coord())
print(p3d1.get_format_coord())
sum_p3d = p3d + p3d1
print(sum_p3d)
