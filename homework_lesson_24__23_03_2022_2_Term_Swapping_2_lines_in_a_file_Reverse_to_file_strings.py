### Term 1 ###
print("Задание 1: Обмен Местами 2 СТРОК в Файле.")

sttr = "Замена строк в текстовом файле;\nизменить строку в списке;\nзаписать список в  файл;"
homework24_task1 = 'homework24_task1.txt'
with open(homework24_task1, 'w') as string3:
    string3.write(sttr)
pos1 = 1
pos2 = 2
copy_line_pos1 = ""
copy_line_pos2 = ""
ind_pos1 = 0
ind_pos2 = 0
with open(homework24_task1, 'r+') as string3:
    rd = string3.readlines()
    for i in range(len(rd)):
        if i == pos1:  # or i == pos2 and pos1 > pos2:
            ind_pos1 = i
            copy_line_pos1 += rd[i]
        if i == pos2:  # or i == pos2 and pos1 > pos2:
            ind_pos2 = i
            copy_line_pos2 += rd[i]
    for i in range(len(rd)):
        if i == pos1:
            rd[i] = copy_line_pos2
        if i == pos2:
            rd[i] = copy_line_pos1
print(ind_pos1)
print(copy_line_pos1)
print(ind_pos2)
print(copy_line_pos2)
# with open(homework24_task1, 'w') as string3:
#     # rd = string3.readlines()
#     for i in range(len(string3)):
#         if i == pos1:
#             rd[i] = copy_line_pos2
#         if i == pos2:
#             rd[i] = copy_line_pos1
with open(homework24_task1, 'r') as string3:
    print(string3.readlines())
    # for line in string3:
    #     print(line)
print()
print()

### Task 2 ###
print("Задание 2: Реверсирование СТРОК Файла ( Перестановка СТРОК Файла в Обратном Порядке )")
sttr = "Замена строк в текстовом файле;\nизменить строку в списке;\nзаписать список в  файл;"
homework24_task2 = 'homework24_task2.txt'
with open(homework24_task2, 'w+') as hw24:
    hw24.write(sttr)

    print(hw24.read())