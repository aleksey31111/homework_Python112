### Term 1 ###
print("Задание 1: Дана СТРОКА СИМВОЛОВ, где Есть ОДНА ОТКР и ЗАКР СКОБКИ."
      "Вывести СИМВОЛЫ Расположенные Внутри этих СКОБОК.")
print()
str2 = "Дана ст(рока символов, среди которых есть одна открыв)ающаяся"
if str2.index('(') < str2.index(')'):
    s2 = str2[str2.find('(') + 1:str2.find(')')]
else:
    s2 = str2[str2.find(')') + 1:str2.find('(')]
print(s2)
print()
print()

### Term 2 ###
print("Задание 2: 1) Найти в СТРОКЕ Указанную ПОДСТРОКУ.\n"
      "         2) Заменить ЕЕ на НОВУЮ.\n"
      "СТРОКУ, ЕЕ ПОДСТРОКУ для Замены и НОВУЮ ПОДСТРОКУ Вводит Пользователь.\n")


def change_num(s, new, old):
    buffer_str_1 = ""
    char = 0
    while char < len(s):
        if s[char] == old[0]:
            buffer_str_1 += new[0]
            buffer_str_1 += new[1]
        elif s[char] == old[1]:
            buffer_str_1 += new[2]
        else:
            buffer_str_1 += s[char]

        char += 1

    return buffer_str_1


str1 = "11 23 44 55 23 22"
str2 = change_num(str1, '!!!', '23')
print("str1 = " + str1)
print("str2 = " + str2)
print()
print()

# ### Term 3 ###
print("Задание 3: В СТРОКЕ Содержащей РУСКОЯЗЫЧНЫЙ ТЕКСТ, Найти Количество СЛОВ, Начинаюшихся с БУКВЫ 'е'.")
piece_of_poetre = (
    f"Ежевику для ежат"
    f"Принесли два ежа."
    f"Ежевику еле-еле"
    f"Ежата возле ели съели."
)
list_piece_of_poetre = list(piece_of_poetre)
e = "е"
E = "Е"
print(e, end=";")
print(E, end=";")
ord_e = ord(e)
ord_E = ord(E)
print(ord("е"), end=";")
print(ord("Е"), end=";")
print(piece_of_poetre.count("Е"), end=";")
print(piece_of_poetre.count("е"), end=";")
print(piece_of_poetre.find(e), end=";")
print(piece_of_poetre.find(E), end=";")
print(len(piece_of_poetre))
print(list(filter(lambda start_e: start_e.startswith(e), piece_of_poetre)))
# for letter_e in piece_of_poetre:
# number_e = 0
# for char_e in piece_of_poetre:
#     # number_e = 0
# # if ord(piece_of_poetre[char_e]) == ord_e and piece_of_poetre[char_e] == ord_E and char_e - 1 == chr(
# #         64) or char_e - 1 == chr(10):
# #     number_e += 1
# #     if ord(piece_of_poetre[char_e]) == ord_e and piece_of_poetre[char_e] == ord_E and char_e - 1 == chr(
# #         64) or char_e - 1 == chr(10):
#     if char_e == e and len(char_e) - 1 != :
#         number_e += 1
# print(number_e)
# char_e = 0
# while char_e < len(piece_of_poetre):
#     if ord(piece_of_poetre[char_e]) == ord_e or ord(piece_of_poetre[char_e]) == ord(E)  and \
#             piece_of_poetre[char_e - 1] != chr(0) and piece_of_poetre[char_e - 1] != chr(64) and \
#             piece_of_poetre[char_e - 1] != chr(64):
#         print(char_e, end=";")
#     char_e += 1

# char_e = 0
# while char_e < len(piece_of_poetre):
#     if ord(piece_of_poetre[char_e]) == ord_e:  # and \
#             # piece_of_poetre[char_e - 1] != chr(0) and piece_of_poetre[char_e - 1] != chr(64) and \
#             # piece_of_poetre[char_e - 1] != chr(64):
#         print(piece_of_poetre.find(e))
#     elif ord(piece_of_poetre[char_e]) == ord(E):
#         print(piece_of_poetre.find(E))
#         char_e += 1

# if
# print(piece_of_poetre.cou)
# print(number_e)
