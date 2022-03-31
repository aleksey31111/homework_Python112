### Term 1 ###
print("Задание 1: Обмен Местами 2 СТРОК в Файле.")
print()
sttr = "Замена строк в текстовом файле;\nизменить строку в списке;\nзаписать список в  файл;"
homework24_task1 = 'homework24_task1.txt'
pos1 = 1
pos2 = 2
if pos2 <= pos1:
    exit()
with open(homework24_task1, 'w') as file:
    file.write(sttr)

with open(homework24_task1, 'r') as file:
    rd = file.readlines()

    s = rd[len(rd) - 1]
    length = len(s)
    f_n = True
    if length > 0 and s[length - 1] != '\n':
        rd[len(rd) - 1] += '\n'
        f_n = False

if pos1 < 0 or pos1 >= len(rd) or pos2 < 0 or pos2 >= len(rd):
    exit()

s = rd[pos1]
rd[pos1] = rd[pos2]
rd[pos2] = s

with open(homework24_task1, 'w') as file:
    if f_n == False:
        rd[len(rd) - 1] = rd[len(rd) - 1][:-1]

    for wr in rd:
        file.write(wr)

with open(homework24_task1, 'r') as file:
    for r in rd:
        print(r)

print()
print()

### Task 2 ###
print("Задание 2: Реверсирование СТРОК Файла ( Перестановка СТРОК Файла в Обратном Порядке )")
sttr = "Замена строк в текстовом файле;\nизменить строку в списке;\nзаписать список в  файл;"
homework24_task2 = 'homework24_task2.txt'

# with open(homework24_task2, 'w') as hw24:
#     hw24.write(sttr)
#
# f = open(homework24_task2, 'r')
# rd = f.readlines()
#
# s = rd[len(rd) - 1]
# length = len(s)
# f_nl = True
#
# if length > 0 and s[length - 1] != '\n':
#     rd[len(rd) - 1] += '\n'
#     f_nl = False
# f.close()
#
# L2 = []
# i = 0
# while i < len(rd):
#     s = rd[len(rd) - i -1]
#     L2 = L2 + [s]
#     i = i + 1
#
# if f_nl == False:
#     L2[len(rd) - 1] = L2[len(rd) - 1][:-1]
#
# f = open(homework24_task2, 'w')
# for item in L2:
#     f.write(item)
# f.close()
#
# f = open(homework24_task2, 'r')
# f.readlines()


# with open(homework24_task2, 'w') as hw24:
#     hw24.write(sttr)
#
# with open(homework24_task2, 'r') as hw24:
#     rd_file = hw24.readlines()
#
#     st = rd_file[len(rd_file) - 1]
#     length = len(st)
#     hw24_newline = True
#
#     if length > 0 and st[length - 1] != '\n':
#         rd_file[len(rd_file) - 1] += '\n'
#         hw24_newline = False
#
# rd_file2 = []
# index = 0
# while index < len(rd_file):
#     st = rd_file[len(rd_file) - index - 1]
#     rd_file2 = rd_file2 + [st]
#     index = index + 1
#
# if hw24_newline == False:
#     rd_file2[len(rd_file) - 1] = rd_file2[len(rd_file) - 1][:-1]
#
# with open(homework24_task2, 'w') as hw24:
#     for w in rd_file2:
#         hw24.write(w)
#
# with open(homework24_task2, 'r') as hw24:
#     for r in rd_file:
#         print(r)

    # print(hw24.read())
