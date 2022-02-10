### Term 1 ###
print("Задание 1: Найти все буквы в первой строке, которых нет во второй.")
first_string = input("Ввдите первую строку: ")
second_string = input("Ввдите вторую строку: ")
first_string_tuple = tuple(first_string)
second_string_tuple = tuple(second_string)
print(first_string_tuple - second_string_tuple)
print()
print()
### Term 2 ###
print("Задание 2: Посчитать гласные буквы в строке.")
input_str = input("Введите строку: ")
tuple_input_str = tuple(input_str)