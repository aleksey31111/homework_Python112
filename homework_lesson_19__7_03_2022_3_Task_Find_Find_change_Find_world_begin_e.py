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
        if s[char] == old[0] and s[char+1]==old[1]:
            buffer_str_1 += new[0]
            buffer_str_1 += new[1]
        elif s[char] == old[1] and s[char-1] == old[0]:
            buffer_str_1 += new[2]
        else:
            buffer_str_1 += s[char]

        char += 1

    return buffer_str_1


str1 = "11 23 44 55 23 22"
str2 = change_num(str1[::-1], '!!!', '32')
print(f"str1 = {str1}")
print(f"str2 = {str2[::-1]}")

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
e = "е"
E = "Е"
count_e = 0
for char_e in range(len(piece_of_poetre)):
    if piece_of_poetre[char_e] == e and ord(piece_of_poetre[char_e - 1]) == 32:
        count_e += 1

count_E = 0
for char_E in range(len(piece_of_poetre)):
    if piece_of_poetre[char_E] == E:
        count_E += 1
print()
print(f"Количество слов: {count_e + count_E}")
