### Term 1 ###
print("Задание 1: Найти все буквы в первой строке, которых нет во второй.")
first_string = input("Ввдите первую строку: ")
second_string = input("Ввдите вторую строку: ")
first_string_set = set(first_string)
second_string_set = set(second_string)


def first_difference_second(first_string_set, second_string_set):
    result_string_set = first_string_set - second_string_set
    return result_string_set


print("Искомыми буквами являются: ")
for i in first_difference_second(first_string_set, second_string_set):
    print(i, end=" ")
print()
print()
### Term 2 ###
print("Задание 2: Посчитать гласные буквы в строке.")
input_str = input("Введите строку: ")
tuple_input_str = tuple(input_str)


def count_vowel(tuple_input_str):
    # set_vowel_1 = {"A", "E", "I", "O", "U", "Y", "a", "e", "i", "o", "u", "y"}
    # set_vowel_2 = {"а","А","е","Е","ё","Ё","и","И","о","О","у","У","ы","Ы","э","Э","ю","Ю","я","Я"}
    tuple_vowel_1 = ("A", "E", "I", "O", "U", "Y", "a", "e", "i", "o", "u", "y")
    tuple_vowel_2 = ("а", "А", "е", "Е", "ё", "Ё", "и", "И", "о", "О", "у", "У", "ы", "Ы", "э", "Э", "ю", "Ю", "я", "Я")
    count = 0
    for letter in tuple_input_str:
        if letter in tuple_vowel_1 or letter in tuple_vowel_2:
            count += 1
    return count


print("Количество гласных равно: ", count_vowel(tuple_input_str))
print()
print()

### Term 3 ###
print("Задание 3: Найти все буквы, присутствующих хотя бы в одной строке.")
string_first = set(input("Введите первую строку: "))
string_second = set(input("Введите вторую строку: "))


def union_set(string_first, string_second):
    union_string = string_first | string_second
    return union_string


print("Искомыми буквами являются: ")
for i in union_set(string_first, string_second):
    print(i, end=" ")
print()
print()

### Term 4 ###
print("Задание 4: Вывод уникальных букв из двух строк.")
# one_tuple_from_strings = tuple(input("Введите первую строку: "))
# two_tuple_from_strings = tuple(input("Введти вторую строку: "))
one_set_from_strings = set(input("Введите первую строку: "))
two_set_from_strings = set(input("Введти вторую строку: "))


def unique_letter(one_set_from_strings, two_set_from_strings):
    # one_set_from_strings, two_set_from_strings = set(one_tuple_from_strings), set(two_tuple_from_strings)
    three_set_from_strings = one_set_from_strings ^ two_set_from_strings
    return three_set_from_strings


print("Искомыми буквами являются: ")
for i in unique_letter(one_set_from_strings, two_set_from_strings):
    print(i, end=" ")
