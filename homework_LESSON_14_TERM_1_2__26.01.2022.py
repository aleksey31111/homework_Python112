from random import randrange, randint

### Term 1 ###
print("Задание 1: Найти наименьший Элемент Из СЛУЧАЙНОЙ МАТРИЦЫ")
size_matrix = int(input("Размерность массива: "))
rand_matrix = [[randrange(1, 100) for col in range(size_matrix)] for row in range(size_matrix)]
min_element = 55
#print(len(rand_matrix))
print("Размерность массива: %d" % size_matrix)
print("Массив из случайных чисел от 0 до 100")
for row in rand_matrix:
    for col in row:
        print(col, end="\t\t")
    print()
print()
print()
for row in rand_matrix:
    for col in row:
        if col < min_element:
            min_element = col
print("Минимальный элемент массива: {0}".format(min_element))

### Term 2 ###
print("Задание 2: Четные строки Двумерного Списка 6х6 заменить Одномерным Списком из 6 Чисел")
# from random import randrange
matrix = [[randrange(10) for col in range(6)]for row in range(6)]
onedimention_list = [randrange(10) for elem in range(6)]
for row in matrix:
    for col in row:
        print(col, end="\t")
    print()
print(onedimention_list)

for row in range(len(matrix)):
    if row % 2 == 0:
        row = onedimention_list
    else:
        row = matrix[row]
    for col in row:
        print(col, end="\t")
    print()
