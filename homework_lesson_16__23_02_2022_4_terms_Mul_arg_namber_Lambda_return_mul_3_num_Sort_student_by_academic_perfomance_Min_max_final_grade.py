### Term 1 ###
print(
    "Задание 1: Написать вложенную функцию, Принимающую на каждую по Одному Аргументу, которые впоследствии перемножаются."
)


def func_compute(multiplier1):
    def multiplication(multiplier2):
        return multiplier1 * multiplier2

    return multiplication


res = func_compute(2)
print(res(15))
print(res(20))
res = func_compute(3)
print(res(15))
print(res(20))
print()
print()

### Term 2 ###
print("Задание 2: Лямбда-Выражение Возвращающее произведение 3 чисел.")

print((lambda x, y, z: x * y * z)(2, 5, 5))
print()
print()
### Term 3 ###
print("Задание 3: Отсортировать список Объектов пл Имени Студентов и Итоговым Оценкам в Порядке Убывания.")

students_lists1 = [{'name': 'Jenifer', 'final': 95},
                   {'name': 'David', 'final': 92},
                   {'name': 'Nikolas', 'final': 98}]
name_descending_order = sorted(students_lists1, key=lambda name: name['name'])
print(name_descending_order)
academic_perfomance_descending_order = sorted(students_lists1,
                                              key=lambda academic_perfomance: academic_perfomance['final'],
                                              reverse=True)
print(academic_perfomance_descending_order)

print()
print()

### Term 4 ###
print("Задание 4: Получить Минимальную и Максимальную Оценку Студента.")

border = [{'name': 'Jenifer', 'final': 95},
          {'name': 'David', 'final': 92},
          {'name': 'Nikolas', 'final': 98}]

grade = sorted(border, key=lambda x: x['final'])
minimal_grade = grade[0]
maximal_grade = grade[-1]
print(maximal_grade)
print(minimal_grade)
