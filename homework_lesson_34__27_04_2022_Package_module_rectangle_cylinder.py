### TASK 1 ###
print("Создать Класс Прямоугольник, Свойства - Длины Сторон,\n"
      "Методы - Вычисление Периметра и Площади Прямоугольника.\n"
      "\tСоздать Производный от Них Класс Цилиндр,\n"
      "\t Свойста -Радиус Основания и Высота\n"
      "\tМетоды - Вычисление Объема Цилиндра,\n"
      "\t Вывод Информации о Фигуре.")
print()

from rectangle_and_cylinder_34 import *

rc1 = cylinder.Cylinder(2, 3, 5, 9)
rc2 = cylinder.Cylinder(6, 7, 2, 3)
rc3 = cylinder.Cylinder(1, 2, 6, 4)
rc4 = cylinder.Cylinder(4, 4, 2, 2)
list_rc = [rc1, rc2, rc3, rc4]
for rci in list_rc:
    print(rci.info())

print('***' * 30)

list_radius = [rc1.base_radius, rc2.base_radius, rc3.base_radius, rc4.base_radius]
print(f"Окружность с наибольшей площадью: Радиус: {max(list_radius)}")

list_perimetr = [rc1.perimetr(), rc2.perimetr(), rc3.perimetr(), rc4.perimetr()]
# print(min(list_perimetr))
print(f"Прямоугольник с наименьшим периметром: Стороны: {rc3.ab}, {rc3.bc}")

print(f"Средний объем всех цилиндров: {round((rc1.volume() + rc2.volume() + rc3.volume() + rc4.volume()) / 4, 2)}")
