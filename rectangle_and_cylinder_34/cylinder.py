from math import pi

### TASK 1 Lesson 34 Cylinder ###
import verify_side_radius_34.verify_cylinder_radius
import verify_side_radius_34.verify_rectangle_side
from rectangle_and_cylinder_34 import rectangle


class Cylinder(rectangle.Rectangle):
    base_radius = verify_side_radius_34.verify_cylinder_radius.Verify_cylinder_radius()
    # ab = verify_side_radius_34.verify_rectangle_side.Verify_rectangle_side()
    height = verify_side_radius_34.verify_rectangle_side.Verify_rectangle_side()

    def __init__(self, ab, bc, base_radius, height):
        super().__init__(ab, bc)
        self.base_radius = base_radius
        self.height = height

    def perimetr(self):
        super().perimetr()
        return self.bc * 2 + self.bc * 2

    def volume(self):
        # return pi * pow(self.radius, 2) * self.bc
        return pi * pow(self.base_radius, 2) * self.height

    def info(self):
        return (f"Длинна окружности: {round(2 * pi * self.base_radius)}\n"
                f"Периметр: {self.perimetr()}\n"
                f"Площадь круга: {round(2 * pi * pow(self.base_radius, 2), 2)}\n"
                f"Объем: {round(self.volume(), 2)}")


__author__ = "啊勒克萨雅"
if __name__ == "__main__":
    print(f"Модуль {__name__} (Автор: {__author__})")
