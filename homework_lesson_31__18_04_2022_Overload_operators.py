class Clock:
    __DAY = 86400
    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError("Секунда Должны быть Числом")

        self.__sec = sec

    def get_format_time(self):
        s = self.__sec % 60  # Second
        m = (self.__sec // 60) % 60  # Minute
        h = (self.__sec // 3600) % 24  # Hour
        return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def get_seconds(self):
        return self.__sec

    def __sub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый Операнд Должен Быть Типом Данных Clock")
        return Clock(self.__sec - other.get_seconds())

    def __mul__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый Операнд Должен Быть Типом Данных Clock")
        return Clock(self.__sec * other.get_seconds() )

    def __floordiv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый Операнд Должен Быть Типом Данных Clock")
        return Clock(self.__sec // other.get_seconds())

    def __mod__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый Операнд Должен Быть Типом Данных Clock")
        return Clock(self.__sec % other.get_seconds())

    def __isub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый Операнд Должен Быть Типом Данных Clock")
        return Clock(self.__sec - other.get_seconds())

    def __imul__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый Операнд Должен Быть Типом Данных Clock")
        self.__sec *= other.get_seconds()
        return self

    def __ifloordiv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый Операнд Должен Быть Типом Данных Clock")
        return Clock(self.__sec // other.get_seconds())

    def __imod__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый Операнд Должен Быть Типом Данных Clock")
        self.__sec %= other.get_seconds()
        return self



c1 = Clock(600)
c2 = Clock(250)
print(f"c1: {c1.get_format_time()}")  # 1
# print(c2.get_format_time())
c3 = c1 - c2
print(f"c1 - c2: {c3.get_format_time()}")  # 2
c4 = c1 * c2
print(f"c1 * c2: {c4.get_format_time()}")  # 3
c5 = c1 // c2
print(f"c1 // c2: {c5.get_format_time()}")  # 4
c6 = c1 % c2
print(f"c1 % c2: {c6.get_format_time()}")  # 5
c1 -= c2
print(f"c1 -= c2: {c1.get_format_time()}")  # 6
c1 = Clock(600)
c1 *= c2
print(f"c1 *= c2: {c1.get_format_time()}")  # 7
c1 = Clock(600)
c1 //= c2
print(f"c1 //= c2: {c1.get_format_time()}")  # 8
c1 = Clock(600)
c1 %= c2
print(f"c1 %= c2: {c1.get_format_time()}")  # 9
