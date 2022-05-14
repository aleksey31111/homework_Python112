### TASK 1 Lesson 34 Rectangle ###

import verify_side_radius_34.verify_cylinder_radius
import verify_side_radius_34.verify_rectangle_side
from abc import ABC, abstractmethod


class Rectangle(ABC):
    ab = verify_side_radius_34.verify_rectangle_side.Verify_rectangle_side()
    bc = verify_side_radius_34.verify_rectangle_side.Verify_rectangle_side()

    def __init__(self, ab, bc):
        self.ab = ab
        self.bc = bc

    @abstractmethod
    def perimetr(self):
        pass

    def volume(self):
        return self.ab * self.bc

    @abstractmethod
    def info(self):
        # return f"Периметр: {self.perimetr()}"
        pass


__author__ = "Алексей"
if __name__ == "__main__":
    print(f"Модуль {__name__} (Автор: {__author__}).")
