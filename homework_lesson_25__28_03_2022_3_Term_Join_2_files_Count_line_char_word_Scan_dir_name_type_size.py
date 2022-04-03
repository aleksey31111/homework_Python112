### Task 1 ###
print("Задание 1: Обьединение Двух Файлов.")
file1 = "file1.txt"
file2 = "file2.txt"
union_file = "union_file.txt"
str1 = "Объектно-ориентированное программирование (ООП) — парадигма программирования,"\
        "в которой основными концепциями являются"\
        "понятия объектов и классов."
str2 = "Класс — тип, описывающий устройство объектов."\
    "Объект — это экземпляр класса."\
    "Класс можно сравнить с чертежом, по которому создаются объекты."
with open(file1, 'w') as f1, open(file2, 'w') as f2:
    f1.write(str1)
    f2.write(str2)

with open(file1, 'r') as f1, open(file2, 'r') as f2, open(union_file, 'w') as file_union:
    rd1 = f1.readlines()
    rd2 = f2.readlines()
    rd_union = rd1 + rd2
    for i in rd_union:
        file_union.writelines(rd_union)

with open(union_file, 'r+') as file_union:
    # for i in rd_union:
    print(file_union.read())
print()

### Task 2 ###
print("Задание 2: В Текстовом Файле Посчитать количество строк, а\n"\
      "также для Каждой Отдельной Строки Определить Количкство в Ней\n"\
      "СИМВОЛОВ и СЛОВ.")
import re
text = "Попробуем определить собственный класс.\n" \
       "создать несколько экземпляров этого класса.\n" \
       "Классу возможно задать собственные методы\n" \
       "Данные структурируются в виде объектов, каждый из\n" \
       "которых имеет определенный тип,\n" \
       "то есть принадлежит к какому-либо классу.\n" \
        "Классы – результат формализации решаемой задачи, выделения главных ее аспектов.\n"\
        "Внутри объекта инкапсулируется логика работы с относящейся к нему информацией.\n"\
        "Объекты в программе взаимодействуют друг с другом, обмениваются запросами и ответами.\n"\
        "При этом объекты одного типа сходным образом отвечают на одни и те же запросы.\n"\
        "Объекты могут организовываться в более сложные структуры, например,\n" \
        "включать другие объекты или наследовать от одного или нескольких объектов."
count_str = 0
count_char = 0
count_word = 0
hw25_task2 = "homework24_task1.txt"
with open(hw25_task2, 'w') as hw2:
    hw2.write(text)

with open(hw25_task2, 'r') as hw2:
    rd = hw2.readline()
    while rd != '':
        rd = hw2.readline()
        count_str += 1

    print(f"Количество строк = {count_str}")

f = open(hw25_task2, 'r')
# for i in f:
rd = f.readline()
rds = f.readlines()
# r = rd.read()
for rl in rds:
    # for r in rl:
    count_word += 1
    if rl == "\\":
        print("первая строка ")

# lst = f.readline().split('\n')
print(rl,end="")
print("Количество слов в строке: ",count_word)
f.close()
        # for ch in w:
        #     count_char += 1
        #
        # print("Количество символов в строке", count_char)