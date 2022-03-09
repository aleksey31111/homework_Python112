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
# string = input("Строка: ")
# substring_for_change = input("Ее заменяемая подстрока: ")
# new_substring = input("Новая подстрока: ")
string = "11 23 44 55 23 22"
substring_for_change = "23"
new_substring = "!!!"
new_substring_in_string = []
for world in string:
    if substring_for_change.find(world) != -1:
        itr = iter(string)
        second = next(itr)
        if second == substring_for_change[1]:
            new_substring_in_string = string[:substring_for_change.find(world)]+substring_for_change+[substring_for_change.find(world)+1]
print(new_substring_in_string)
#     start_index_substring_for_change = string.find(substring_for_change)
#     start_index_substring_for_change_2 = string.find(substring_for_change, start_index_substring_for_change + 1)
# index_of_substring = [ind for ind in range(len(string))]
# print(index_of_substring)
#     start_index_substring_for_change = string.find(world)
#     if string[world] == substring_for_change[0]:
#         print(world)
# itr = iter(string)
# print(next(itr))

    # print(world)
# print(world)
# print(start_index_substring_for_change)
# print(start_index_substring_for_change_2)