####
#### TERM 1: Find MAX POSITIVE Namber from Positive and Negative List ####
####
## 1 - Вариант выводит в списке положительных чисел отрицательное.
# gen_pos_neg_nam = [int(input("Введите элемент списка: ")) for i in range(int(input("Введите длину списка: ")))]
# print("Список: {0}".format(gen_pos_neg_nam))
# [gen_pos_neg_nam.remove(i) for i in gen_pos_neg_nam if i < 0]

# for i in gen_pos_neg_nam: #Перечисление элемента по одному
#     if i < 0: # Если значение элемента < 0
#         gen_pos_neg_nam.remove(i) # Удаляем отрицательный элемент
# print("Новый список, состоящий из положитеьных элементов: {0}".format(gen_pos_neg_nam), end=" ")
# for i in gen_pos_neg_nam:
#     for j in gen_pos_neg_nam:
#         if i < j:
#             max_namber = j
# print("\nНаибольший элемент списка: %d" % max_namber)

# ## 2 - Вариант ##
print("Задание 1")
gen_pos_neg_nam = [int(input("Введите элемент списка: ")) for i in range(int(input("Введите длину списка: ")))]
print("Список: {0}".format(gen_pos_neg_nam))
positive_namber = list()
max_namber = 0
[positive_namber.append(i) for i in gen_pos_neg_nam if i > 0]
print("Новый список, состоящий из положитеьных элементов: {0}".format(positive_namber), end=" ")
print("\nНаибольший элемент списка: ", max(positive_namber))
print()
print()
# [print("Наибольший элемент списка: %d" % i) for i, j in gen_pos_neg_nam if i > j]
# Неудавшееся сокращение.

####
#### TERM 2: Insert Element with Index "k" and Value C ####
####
print("Задание 2")
print("Введите элементы списка: ")
elements = [int(input("-> ")) for i in range(int(input("n = ")))]
k = int(input("Введите индекс: \nk = "))
c = int(input("Введите значение: \n c = "))
elements.insert(k, c)
print(elements)
print()
print()
####
#### TERM 3: Fill the List of Random namber, and Sorted by DESCENDING ####
####
print("Задание 3")
from random import random
random_list = [round(random()*100) for i in range(11)]
print(random_list)
print(sorted(random_list, reverse=True))
print()
print()
####
#### Term 4: Program, that varificate namber in LIST
####
print("Задание 4")
print("Введите элементы списка: ")
list_from_keyboard = [int(input("-> ")) for i in range(int(input("n = ")))]

ch = int(input("Введите число:\nch =  "))
for i in list_from_keyboard:
    if i != ch:
        continue
    else:
        print("Число присутствует в элементах списка")