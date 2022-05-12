class Verify_cylinder_radius:
    @classmethod
    def whole_float_radius(cls, rad):
        if not isinstance(rad, (int, float)):
            raise TypeError(f"{rad} Должен быть целым числом или вещественным числом")

    @classmethod
    def verify_positive_radius(cls, rad):
        if rad < 0:
            raise ValueError(f"{rad} Должен быть положительным числом")

    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f"{self.__name} должно быть POS")
        instance.__dict__[self.__name] = value
