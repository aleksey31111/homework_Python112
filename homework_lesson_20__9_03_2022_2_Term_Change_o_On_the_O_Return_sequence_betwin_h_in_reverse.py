### Task 1: in 6.jpg ###
print("Задание 1:\n"
      "Замените в этой строке все появления буква \"о\" на букву \"О\",\n"
      "кроме первого и последнего вхождения.")
# str_for_change = (
#     "Замените в этой строке все появления буква \"о\" на букву \"О\", кроме первого и последнего вхождения.")
str_for_change = input("Введите строку: ")
reversed_str_for_change = str_for_change[::-1]
o = "о"
O = "О"
pat = o
slice_o_start = str_for_change[:str_for_change.find(o) + 1]
slice_o_end = str_for_change[str_for_change.rfind(o):]
between_start_o_end = str_for_change[str_for_change.find(o) + 1: str_for_change.rfind(o)]
replace_operate = between_start_o_end.replace(o, O)
full_replaced_string = slice_o_start + replace_operate + slice_o_end
print(full_replaced_string)
print()
print()

### Term 2: ###
print("Задание 2: Развернуть последовательность символов заключенные между буквами 'h' в противоположном порядке.")
# str_for_change_h = "I am learning Python. hello, WORLD!"
str_for_change_h = input("Введите строку: ")
h = 'h'
between_start_h_end = str_for_change_h[str_for_change_h.find(h) + 1: str_for_change_h.rfind(h)]
print(str_for_change_h[:str_for_change_h.find(h)+1] + between_start_h_end[::-1] + str_for_change_h[str_for_change_h.rfind(h):])

