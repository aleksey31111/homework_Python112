### Term 1 ###
print("Задание 1: Создать Класс для Преобразования Килограмм в Фунты\n"
      "12 кг => 26.46 фунтов\n"
      "41 кг => 90.405 фунтов")
print()


class Transformation:
    def __init__(self, weight):
        self.__weight = 0
        if Transformation.__check_value(weight):
            self.__weight = weight
        else:
            print("Неверный Формат Данных")

    def __check_value(val):
        if isinstance(val, (int, float)):
            return True
        return False

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if Transformation.__check_value(weight):
            self.__weight = weight
        else:
            print("Неверный Формат Данных")

    def mapping(self):
        return round(self.__weight * 2.20462, 2)

    # @weight.deleter
    # def weight(self):
    #     del self.__weight


reform = Transformation(12)
print(f"{reform.weight} кг =>  {reform.mapping()} фунтов")
reform.weight = 41
print(f"{reform.weight} кг =>  {reform.mapping()} фунтов")
