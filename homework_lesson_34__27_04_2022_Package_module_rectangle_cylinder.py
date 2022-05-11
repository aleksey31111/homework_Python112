### TASK 1 ###
print("Создать Класс Прямоугольник, Свойства - Длины Сторон,\n"
      "Методы - Вычисление Периметра и Площади Прямоугольника.\n"
      "\tСоздать Производный от Них Класс Цилиндр,\n"
      "\t Свойста -Радиус Основания и Высота\n"
      "\tМетоды - Вычисление Объема Цилиндра,\n"
      "\t Вывод Информации о Фигуре.")
print()

from rectangle_and_cylinder_34 import *

c1 = cylinder.Cylinder(5, 9, 10)
# c1.cylinder_info()
c2 = cylinder.Cylinder(2, 3, 1)
# c2.cylinder_info()
c3 = cylinder.Cylinder(1, 2, 3)
# c3.cylinder_info()
# c4 = cylinder.Cylinder(4, 4, 2)
# c4.cylinder_info()
for cil in [c1, c2, c3]:
    print(cil.cylinder_info_length_cycle_of_base())
for cic in [c1, c2, c3]:
    print(cic.cylinder_info_circle_square_of_base())
for cip in [c1, c2, c3]:
    print(cip.cylinder_info_surface_perimeter())
for cisv in [c1, c2, c3, ]:
    print(cisv.cylinder_infocircle_square_of_base_and_volume())
