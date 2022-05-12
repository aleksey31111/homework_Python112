### TASK 1 Lesson 34 Rectangle ###
from abc import ABC, abstractmethod


class Rectangle(ABC):
    def __init__(self, ab, bc):
        self.ab = ab
        self.bc = bc

    def perimetr(self):
        return self.ab * 2 + self.bc * 2

    def volume(self):
        return self.ab * self.bc

    @abstractmethod
    def info(self):
        # return f"Периметр: {self.perimetr()}"
        pass


__author__ = "Алексей"
if __name__ == "__main__":
    print(f"Модуль {__name__} (Автор: {__author__}).")
