class Clock:
    # DAY = 86400
    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError("Секунда Должны быть Числом")

        self.sec = sec

    def get_format_time(self):
        s = self.sec % 60  # Second
        m = (self.sec // 60) % 60  # Minute
        h = (self.sec // 3600) % 24  # Hour
        return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"

    @staticmethod
    def get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def get_seconds(self):
        return self.sec

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый Операнд Должен Быть Типом Данных Clock")
        return Clock(self.sec + other.get_seconds())


c1 = Clock(100)
c2 = Clock(200)
c3 = c1 + c2
print(c1.get_format_time())
print(c2.get_format_time())
print(c3.get_format_time())
