from random import randrange, randint

### Term 1 ###
print("Задание 1: Найти наименьший Элемент Из СЛУЧАЙНОЙ МАТРИЦЫ")
size_matrix = int(input("Размерность массива: "))
rand_matrix = [[randrange(-100, 100) for col in range(size_matrix)] for row in range(size_matrix)]
positive_rand_matrix = list()
min_element = 55
#print(len(rand_matrix))
print("Размерность массива: %d" % size_matrix)
print("Массив из случайных чисел от -100 до 100")
for row in rand_matrix:
    for col in row:
        print(col, end="\t\t")
    print()
print()
print()
print("Массив из случайных положительных чисел из массива выше")
# positive_rand_matrix = [[col for col in row if col > 0] for row in rand_matrix]
# for row in positive_rand_matrix:
#     for col in row:
#         print(col, end="\t\t")
#     print()
# print()
for row in rand_matrix:
    for col in row:
        if col > 0:
            print(col, end=" ")
            if col < min_element:
                min_element = col
    print()
# for row in rand_matrix:
#     for col in row:
#         if col < min_element:
#             min_element = col
print("Минимальный элемент массива: {0}".format(min_element))

