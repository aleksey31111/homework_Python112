class Verify_rectangle_side:
    @classmethod
    def whole_side(cls, side):
        if not isinstance(side,int):
            raise TypeError(f"{side} Должен быть целым числом")
    @classmethod
    def verify_positive_radius(cls, side):
        if side < 0:
            raise ValueError(f"{side} Должен быть положительным числом")