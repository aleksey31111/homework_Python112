### Term 1 ###
print("Задание 1: Найти все буквы в первой строке, которых нет во второй.")
first_string = input("Ввдите первую строку: ")
second_string = input("Ввдите вторую строку: ")
first_string_set = set(first_string)
second_string_set = set(second_string)


def first_difference_second(first_string_set, second_string_set):
    result_string_set = first_string_set - second_string_set
    result_string_tuple = tuple(result_string_set)
    result_string = [i for i in result_string_tuple]
    return result_string

    # result_string_tuple = tuple(result_string_set)
    # print(result_string_tuple)
    # for i in result_string_tuple:
    #     return i
    # if result_string_tuple.count(i) == 5:
    #     a, b, c, d, e = result_string_tuple
    #     return a, b, c, d, e
    # elif result_string_tuple.count(i) == 4:
    #     a, b, c, d = result_string_tuple
    #     return a, b, c, d
    # if result_string_tuple.count(i) == 3:
    #     x, y, z = result_string_tuple
    #     return x, y, z
    # elif result_string_tuple.count(i) == 2:
    #     x, y = result_string_tuple
    #     return x, y
    # elif result_string_tuple.count(i) == 1:
    #     return i


print("Искомыми буквами являются: ", first_difference_second(first_string_set, second_string_set))
print()
print()
### Term 2 ###
print("Задание 2: Посчитать гласные буквы в строке.")
input_str = input("Введите строку: ")
set_input_str = set(input_str)


def count_vowel(set_input_str):
    set_vowel = {"A", "E", "I", "O", "U", "Y", "a", "e", "i", "o", "u", "y"}
    count = 0
    for letter in set_input_str:
        if letter in set_vowel:
            count += 1
    return count


print("Количество гласных равно: ", count_vowel(set_input_str))
print()
print()

### Term 3 ###
print("Задание 3: Найти все буквы, присутствующих хотя бы в одной строке.")
string_first = set(input("Введите первую строку: "))
string_second = set(input("Введите вторую строку: "))


def union_set(string_first, string_second):
    union_string = string_first | string_second
    return union_string


union_string_set = union_set(string_first, string_second)
# for i in union_string_set:
#     union_string_list = list()
#     union_string_list.append(i)
# for i in union_string_list:
print("Искомыми буквами являются: ", union_string_set)
print()
print()

### Term 4 ###
print("Задание 4: Вывод уникальных букв из двух строк.")
one_tuple_from_strings = tuple(input("Введите первую строку: "))
two_tuple_from_strings = tuple(input("Введти вторую строку:"))


def unique_letter(one_tuple_from_strings, two_tuple_from_strings):
    one_set_from_strings, two_set_from_strings = set(one_tuple_from_strings), set(two_tuple_from_strings)
    three_set_from_strings = one_set_from_strings ^ two_set_from_strings
    return three_set_from_strings


value_simmetric_difference = unique_letter(one_tuple_from_strings, two_tuple_from_strings)
print("Искомыми буквами являются: ", value_simmetric_difference)
