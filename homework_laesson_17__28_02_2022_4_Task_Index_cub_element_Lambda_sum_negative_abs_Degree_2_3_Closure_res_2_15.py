### Task 1 ###
print("Задание 1: Получить новый список из старого, \n"
      "путем Умножения ЭЛЕМЕНТА старого списка \n"
      " на ЕГО ИНДЕКС возведенный в 3 степень.")
nambers_sequence_1 = [0, 6, 8, 9, 1, 2]
length_nambers_sequence_1 = []
for i in range(len(nambers_sequence_1)):
    length_nambers_sequence_1.append(i)
length_namber_cub_1 = list(map(lambda length: length * length * length, length_nambers_sequence_1))
new_nambers_sequence_1 = list(map(lambda namber, length: namber * length, nambers_sequence_1, length_namber_cub_1))
print(str(nambers_sequence_1) + "  -> " + str(new_nambers_sequence_1))
print()
print(new_nambers_sequence_1)
print()
print()

### Task 2 ###
print("Задание 2: Удалить из Списка все положительные числа, Найти СУММУ Отрицательных, Вывести Абсолютное Значение. ")
print("Вариант 1: Цикл for.")
nambers_sequence2 = [3, -4, -6, 7, -8, 3, -12, 4, 7]
print("l = " + str(nambers_sequence2))
print()
for namber in nambers_sequence2:
    if namber > 0:
        nambers_sequence2.remove(namber)
        for namber in nambers_sequence2:
            if namber > 0:
                nambers_sequence2.remove(namber)
print(nambers_sequence2)
print(abs(sum(nambers_sequence2)))
print()
print("Вариант 2: list(filter(lambda))")
nambers_sequence2 = [3, -4, -6, 7, -8, 3, -12, 4, 7]
nambers_sequence2_without_positive = list(filter(lambda positive: positive < 0, nambers_sequence2))
print("l = " + str(nambers_sequence2))
print()
print(nambers_sequence2_without_positive)
print(abs(sum(nambers_sequence2_without_positive)))
print()
print()

### Task 3 ###
print("Задание 3: Используя lambda-выражения Возвести в КВАДРАТ и в КУБ все элементы списка.")
nums = [3, 5, 7, 3, 9, 5, 7, 2]
nums_square = list(map(lambda num: num * num, nums))
nums_cub = list(map(lambda num: num * num * num, nums))
print("nums = " + str(nums))
print()
print(nums_square)
print(nums_cub)
print()
print()


### Task 4 ###
print("Задание 4: Написать ФУНКЦИЮ, Принимающей ОДИН АРГУМЕНТ,"
      "который в дальнейшем Будет Умножаться на ЗАДАННОЕ ЧИСЛО.")


def func_compute(num1):
    def given_arg(num2):
        return num1 * num2
    return given_arg


res = func_compute(2)
print(res(15))
print(res(20))
res = func_compute(3)
print(res(15))
print(res(20))