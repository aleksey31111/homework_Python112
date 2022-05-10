### TASK 1 Lesson 34 Rectangle ###
class Rectangle:
    def __init__(self, ab, bc):
        if not isinstance(ab, int) or not isinstance(bc, int):
            self.ab = ab
            self.bc = bc
            # self.cd = cd
            # self.da = da

    def rect_per(self):
        return self.ab * 2 + self.bc * 2

    def rect_square(self):
        return self.ab * self.bc


__author__ = "Алексей"
if __name__ == "__main__":
    print(f"Модуль {__name__} (Автор: {__author__}).")