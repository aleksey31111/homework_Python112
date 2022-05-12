class Verify_cylinder_radius:
    @classmethod
    def whole_float_radius(cls, rad):
        if not isinstance(rad, (int, float)):
            raise TypeError(f"{rad} Должен быть целым числом или вещественным числом")

    @classmethod
    def verify_positive_radius(cls, rad):
        if rad < 0:
            raise ValueError(f"{rad} Должен быть положительным числом")
