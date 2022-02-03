from math import sin, pi


### Term 1 ###
def square_of_rectangle(base_rectangle, height_rectangle):
    print("Площадь: {0}".format(round(float(base_rectangle * height_rectangle)), 2))


def square_of_triangle(base_triangle, height_triangle):
    print("Площадь: {0}".format(round(float(base_triangle * height_triangle / 2)), 2))


def square_of_circle(radius):
    print("Площадь: {0}".format(round(float(2 * pi * pow(radius, 2))), 2))


print("Задание 1: Напишите Функции нахождения Площади Фмгур",
      "1 - прямоугольник, 2 - треугольник, 3 - круг.")
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
