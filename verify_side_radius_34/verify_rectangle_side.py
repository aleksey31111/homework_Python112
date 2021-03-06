class Verify_rectangle_side:
    @classmethod
    def whole_side(cls, side):
        if not isinstance(side, int):
            raise TypeError(f"{side} Должен быть целым числом")

    @classmethod
    def verify_positive_radius(cls, side):
        if side < 0:
            raise ValueError(f"{side} Должен быть положительным числом")

    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f"{self.__name} должно быть POS")
        instance.__dict__[self.__name] = value
