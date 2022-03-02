### Task 1 ###
print("Задание 1: Получить новый список из старого, \n"
      "путем Умножения ЭЛЕМЕНТА старого списка \n"
      " на ЕГО ИНДЕКС возведенный в 3 степень.")
nambers_sequence1 = [0, 6, 8, 9, 1, 2]
length_nambers_sequence1 = []
for i in range(len(nambers_sequence1)):
    length_nambers_sequence1.append(i)
length_namber_cub1 = list(map(lambda length: length * length * length, length_nambers_sequence1))
new_nambers_sequence = list(map(lambda namber, length: namber * length, nambers_sequence1, length_namber_cub1))
print(new_nambers_sequence)
print()
print()

### Task 2 ###
print("Задание 2: Удалить из Списка все положительные числа, Найти СУММУ Отрицательных, Вывести Абсолютное Значение. ")
# nambers_sequence2 =