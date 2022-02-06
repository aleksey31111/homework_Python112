from math import pi
from random import randint

### Term 1: Square of figure ###
# print("Задание 1: Напишите Функции нахождения Площади Фмгур",
#       "1 - прямоугольник, 2 - треугольник, 3 - круг.")

def square_of_rectangle(base_rectangle, height_rectangle):
    # print("Площадь: {0}".format(round(float(base_rectangle * height_rectangle)), 2))
    # square_rect = round(float(base_rectangle * height_rectangle), 2)
    print("Площадь: {0}".format(round(float(base_rectangle * height_rectangle), 2)))


def square_of_triangle(base_triangle, height_triangle):
    print("Площадь: {0}".format(round(float(base_triangle * height_triangle / 2), 2)))


def square_of_circle(radius):
    print("Площадь: {0}".format(round(float(2 * pi * pow(radius, 2)), 2)))


figure = int(input("1-прямоугольник, 2-треугольник, 3-круг: "))
if figure == 1:
    b = int(input("Основание: "))
    h = int(input("Высота: "))
    square_of_rectangle(b, h)
elif figure == 2:
    b = int(input("Основание: "))
    h = int(input("Высота: "))
    square_of_triangle(b, h)
elif figure == 3:
    r = int(input("Радиус окружности: "))
    square_of_circle(r)
else:
    print("Такой фигуры нет в задании.")
print()
print()


### Term 2 : Simple namber - min, Composite namber - max
# print("Задание 2: Найти, минимальное число из Простых чисел и максимальное из Не Простых.")
###### Term 2, without Use any Functions ######
# list_whole_numbers = list()
# simple_numbers = list()
# composite_numbers = list()
# while len(list_whole_numbers) != 13:
#     namber = randint(1, 16)
#     if namber not in list_whole_numbers:
#         list_whole_numbers.extend([namber])
# print(list_whole_numbers)
# for i in list_whole_numbers:
#     if i == 2 or i == 3:
#         simple_numbers.append(i)
#     elif i == 1 or i % 2 == 0 or i % 3 == 0:
#         composite_numbers.append(i)
#     else:
#         simple_numbers.append(i)
# # print("Список из Простых чисел: ", simple_numbers)
# # print("Список из Не Простых чисел: ", composite_numbers)
# print("Min: ", min(simple_numbers))
# print("Max: ", max(composite_numbers))

###### Term 2, with Use Functions ######
list_whole_numbers = list()


def rand_list_whole_namber():
    while len(list_whole_numbers) != 13:
        namber = randint(1, 16)
        if namber not in list_whole_numbers:
            list_whole_numbers.extend([namber])
    return (list_whole_numbers)


def min_simple(list_whole_numbers):
    simple_numbers = list()
    composite_numbers = list()
    for i in list_whole_numbers:
        if i == 2 or i == 3:
            simple_numbers.append(i)
        elif i == 1 or i % 2 == 0 or i % 3 == 0:
            composite_numbers.append(i)
        else:
            simple_numbers.append(i)
    return (min(simple_numbers))


def max_not_simple(list_whole_numbers):
    simple_numbers = list()
    composite_numbers = list()
    for i in list_whole_numbers:
        if i == 2 or i == 3:
            simple_numbers.append(i)
        elif i == 1 or i % 2 == 0 or i % 3 == 0:
            composite_numbers.append(i)
        else:
            simple_numbers.append(i)
    return (max(composite_numbers))


print(rand_list_whole_namber())
print("Min: ", min_simple(list_whole_numbers))
print("Max: ", max_not_simple(list_whole_numbers))
