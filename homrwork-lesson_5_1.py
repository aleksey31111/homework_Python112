import random as r

print("### Задание 1: Найти сумму Элементов 20-размерного Случайного Списка. ###")
lst = [r.randrange(1, 100) for i in range(21)]
print(lst)
print("Summa: %d" % sum(lst))

print("### Задание 2: Транспозиция матрицы. Поменять СТРОКИ и СТОЛБЦЫ местами")
mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print("Исходная матрица: ")
for row in range(len(mat)):
    for col in range(len(mat[row])):
        print(mat[row][col], end="\t")
    print()
print()
print("Транспозиционированная матрица: ")
# transposition_mat = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
print("Вариант 1: ")
print(mat[0][0], mat[1][0], mat[2][0])
print(mat[0][1], mat[1][1], mat[2][1])
print(mat[0][2], mat[1][2], mat[2][2])
print(mat[0][3], mat[1][3], mat[2][3])
print("Вариант 2: ")
transpose_mat = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
# print(transpose_mat)
for row in range(len(transpose_mat)):
    for col in range(len(transpose_mat[row])):
        print(transpose_mat[row][col], end="\t\t")
    print()
print()
print("Вариант 3")
row = 0
for row in mat:
    for col in row:
        print(col, end="\t")
    print()
print("----------------")
i = 0
for row in row:
    for row in mat:
        print(row[i], end="\t")
    i += 1
    print()
print()
print("Задание 3: Заполнить СПИСОК Уникальными СЛУЧАЙНЫМИ ЧИСЛАМИ: ")
print("Вариант 1: ")
unique_lst = list()
while len(unique_lst) != 10:
    namber = r.randint(0, 9)
    if namber not in unique_lst:
        unique_lst.extend([namber])
print(unique_lst)

