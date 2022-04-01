### Term 1 ###
print("Задание 1: Обмен Местами 2 СТРОК в Файле.")
print()
sttr = "Замена строк в текстовом файле;\nизменить строку в списке;\nзаписать список в  файл;"
homework24_task1 = 'homework24_task1.txt'
pos1 = int(input('pos1 = '))
pos2 = int(input('pos2 = '))
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

hw24 = open(homework24_task2, 'w')
hw24.write(sttr)
hw24.close()

for line in reversed(open(homework24_task2).readlines()):
    print(line.rstrip())