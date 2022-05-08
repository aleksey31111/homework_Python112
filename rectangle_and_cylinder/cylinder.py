### TASK 1 Lesson 34 Cylinder ###
from rectangle_and_cylinder import rectangle
class Cylinder(rectangle.Rectangle):
    def __init__(self, ab, bc, cd, da, radius, base, height):
        super().__init__(ab, bc, cd, da)
        self.radius = radius
        self.base = base
        self.height = height