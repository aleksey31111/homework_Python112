### Task 1 ###
print("Задание 1: Обьединение Двух Файлов.")
file1 = "file1.txt"
file2 = "file2.txt"
union_file = "union_file.txt"
str1 = "Объектно-ориентированное программирование (ООП) — парадигма программирования," \
       "в которой основными концепциями являются" \
       "понятия объектов и классов."
str2 = "Класс — тип, описывающий устройство объектов." \
       "Объект — это экземпляр класса." \
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
print("Задание 2: В Текстовом Файле Посчитать количество строк, а\n" \
      "также для Каждой Отдельной Строки Определить Количкство в Ней\n" \
      "СИМВОЛОВ и СЛОВ.")

text = "Попробуем определить собственный класс.\n" \
       "создать несколько экземпляров этого класса.\n" \
       "Классу возможно задать собственные методы\n" \
       "Данные структурируются в виде объектов, каждый из\n" \
       "которых имеет определенный тип,\n" \
       "то есть принадлежит к какому-либо классу.\n" \
       "Классы – результат формализации решаемой задачи, выделения главных ее аспектов.\n" \
       "Внутри объекта инкапсулируется логика работы с относящейся к нему информацией.\n" \
       "Объекты в программе взаимодействуют друг с другом, обмениваются запросами и ответами.\n" \
       "При этом объекты одного типа сходным образом отвечают на одни и те же запросы.\n" \
       "Объекты могут организовываться в более сложные структуры, например,\n" \
       "включать другие объекты или наследовать от одного или нескольких объектов."
# count_str = 0
# count_char = 0
# count_word = 0
hw25_task2 = "homework24_task1.txt"
with open(hw25_task2, 'w') as hw2:
    hw2.write(text)

hw2 = open(hw25_task2)
line = 0
for count_line in hw2:
    line += 1
    flag = 0
    word = 0
    for count_word in count_line:
        if count_word != ' ' and flag == 0:
            word += 1
            flag = 1
        elif count_word == ' ':
            flag = 0
    print(count_line, len(count_line), 'симв.', word, 'сл.')
print(line, 'стр.')
hw2.close()
print()



### Task 3 ###
import os

print("Напишите программу, которая просканирует выбранную дирректорию\n"
      "и для всех ее Обьектов выведет следущую информацию на экран:\n"
      "имя - тип - размер (только для файлов)\n"
      "* Типы Объектов: файл, директория\n"
      "* Размер: только для файлов")
folders = ['choice_dir/test', 'choice_dir/test1']
for fold in folders:
    os.makedirs(fold)
# print(os.listdir("choice_dir"))
for fold in folders:
    print(f"{os.path.split(fold)[1]} - dir")
files = {
    'choice_dir': ['project.txt', 'test.txt'],
}
for fold, fl in files.items():
    for file in fl:
        # file_path = os.path.join(fold, file)
        # print(file_path)
        with open(file, "w") as f:
            f.write(f"{file}\n"
                    f"Можно создавать разные инстансы одного класса \n"
                    f"с заранее заданными параметрами с помощью инициализатора \n"
                    f"(специальный метод __init__). Для примера возьмем класс Point \n"
                    f"(точка пространства), объекты которого должны иметь определенные \n"
                    f"координаты:")
for fold, fl in files.items():
    for file in fl:
        print(f"{file} - file - {os.path.getsize(file)} bytes")
