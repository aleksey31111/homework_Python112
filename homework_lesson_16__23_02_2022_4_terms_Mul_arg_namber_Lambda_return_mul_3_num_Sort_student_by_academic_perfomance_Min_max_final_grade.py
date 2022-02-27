### Term 1 ###
print(
    "Задание 1: Написать вложенную функцию, Принимающую на каждую по Одному Аргументу, которые впоследствии перемножаются.")


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

### Term 3 ###
print("Задание 3: Отсортировать список Объектов пл Имени Студентов и Итоговым Оценкам в Порядке Убывания.")

students_lists1 = [{'name': 'Jenifer', 'final': 95},
                   {'name': 'David', 'final': 92},
                   {'name': 'Nikolas', 'final': 98}]


def students1(*args1):
    def sort_name():
        return args1.sort("name")

    def sort_grade():
        return args1.sort("final")

    def buffer_transparent():
        pass

    buffer_transparent.sort_name = sort_name
    buffer_transparent.sort_grade = sort_grade
    return buffer_transparent


students1(students_lists1)  # students1(students_lists1)

#         for student_list1 in args2:
# print(student_list1)
#   for student_list2 in student_list1:
#             # print(student_list2)
#             # def students2(**kwargs1):
#         # for (k1,v1) in kwargs1.items():
#         #     print(k1, v1)
#         #         print(kwargs1)
#                 # return kwargs1
#     # return args2
#
#
# students1(students_lists1)
# def students(*args):
#     print(args)
#     students_lists2 = dict()
#     for student_list1 in args:
#         print(student_list1)
#         for student_list2 in student_list1:
#             print(student_list2)
#             for student_list3 in student_list2:
#                 students_lists2 = dict()
#                 students_lists2 = students_lists2 | student_list3
#             return students_lists2
#             # args.sort()
#     # print(args)
#
#
# students(students_lists1)


# student_dict1 = (tuple(*students_list)
# print(student_dict1)
# def outer(lower, upper):
#     def inner(exam):
#         return {key: value for (key, value) in exam.items()}
#
#
# a = outer(80,90)
# print(a(students_list))
# # students_unpuck_list = *students_list
# # for student_list in students_list:
# #     s_l={}
# #     s_l += student_list
# #     print(s_l)
# #     s_l =| s_l
#     # print(name_final_key, name_final_value)
# # for student, name_grade in student_list.items():
# #     print(student, name_grade)
# students_list_zip = list(students_list)
# print(*students_list)
# def students1(*args):
#     # students11 = args
#     # print(students11)
#     for i in args:
#         print(i)
#     # def students2(**kwargs):
#     #     def sort_name():
#     #         return {key: value for (key, value) in kwargs.items() if key == 'name'}
# #
# #     def sort_evaluation():
# #         # return {student_list.sort(value) for (key, value) in student_list.items() if key == 'final'}
# #         return {}
# #     def buffer_func():
# #         pass
# #
# #     buffer_func.sort_name = sort_name
# #     buffer_func.sort_evaluation = sort_evaluation
# #     return buffer_func
# #
# #
# # students1([{'name': 'Jenifer', 'final': 95}, {'name': 'David', 'final': 92}, {'name': 'Nikolas', 'final': 98}])
# print(students1(students_list))
print()
print()

### Term 4 ###
print("Задание 4: Получить Минимальную и Максимальную Оценку Студента.")


# def border(**kwargs):
#     print(kwargs)


border = [{'name': 'Jenifer', 'final': 95},
           {'name': 'David', 'final': 92},
           {'name': 'Nikolas', 'final': 98}]

def border_grade():
    border.sort('final')
    print(border)