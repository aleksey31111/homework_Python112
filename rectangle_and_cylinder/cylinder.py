from math import pi
### TASK 1 Lesson 34 Cylinder ###
from rectangle_and_cylinder import rectangle


class Cylinder(rectangle.Rectangle):
    def __init__(self, ab, bc, radius):  # , base, height):
        super().__init__(ab, bc)
        self.ab = ab
        self.bc = bc
        self.radius = radius

    def volume_cylinder(self):
        # return pi * pow(self.radius, 2) * self.bc
        return pi * pow(self.radius, 2) * self.bc

    def cylinder_info_length_cycle_of_base(self):
        return (f"Длинна окружности: {round(self.ab * pi, 2)}")

    def cylinder_info_circle_square_of_base(self):
        return (f"Площадь круга: {round(2 * pi * pow(self.radius, 2), 2)}")

    def cylinder_info_surface_perimeter(self):
        return (f"Периметр: {round(pi * pow(self.radius, 2), 2)}")

    def cylinder_infocircle_square_of_base_and_volume(self):
        return (f"Площадь круга: {round(2 * pi * pow(self.radius, 2), 2)}\n"
        f"Объем: {round(self.volume_cylinder(), 2)}")


__author__ = "啊勒克萨雅"
if __name__ == "__main__":
    print(f"Модуль {__name__} (Автор: {__author__})")
# c1 = Cylinder(5, 9, 10)
# c1.cylinder_info()
