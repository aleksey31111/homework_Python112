### Task 1: in 6.jpg ###
import re

print("Задагие 1:\n"
      "Замените в этой строке все появления буква \"о\" на букву \"О\",\n"
      "кроме первого и последнего вхождения.")
str_for_change = (
    "Замените в этой строке все появления буква \"о\" на букву \"О\", кроме первого и последнего вхождения.")
reversed_str_for_change = str_for_change[::-1]
o = "о"
O = "О"
chanded_str = str_for_change.replace(o, O)
print(chanded_str)

print(len(str_for_change))
# find_o_start = str_for_change.find(o)
# find_o_end = reversed_str_for_change.find(o)
# print(find_o_start)
# print(find_o_end)
# changed_str = ""
# print(str_for_change[13], str_for_change[len(str_for_change) - find_o_end-1])
# for ind in range(len(str_for_change)):
#     if ind != 13 and ind != len(str_for_change) - find_o_end - 1:
#         changed_str = str_for_change.replace(o, O)
# if str_for_change[12:15] != find_o_start and str_for_change[len(str_for_change) - find_o_end - 1: len(str_for_change) - find_o_end] != find_o_end:
#     changed_str = str_for_change.replace(o, O)
# print(changed_str)
pat = o
search_o_span = re.search(pat, str_for_change).span()
search_o_start = re.search(pat, str_for_change).start()
search_o_end = re.search(pat, reversed_str_for_change).start()
print(search_o_span)
print(search_o_start)
print(search_o_end)
# changed_str = str_for_change[:search_o_start+1] + 'О'.join(str_for_change.split('о')) + str_for_change[str_for_change.rfind(o):]
split_str_3 = re.split(" ", str_for_change, 3)
print(split_str_3)
reverse_split_str_1 = re.split(' ', reversed_str_for_change, 1)
print(reverse_split_str_1)

# print(changed_str)
