num_char = int(input("Количество символов: "))
type_char = str(input("Тип символа: "))
line_orientation = int(input("ориентация линии: '1-вертикальная или 0-горизонтальная': "))
i = 0
if line_orientation == 0:
    # print(num_char * type_char)
    while i < num_char:
        print(type_char, end="")
        i += 1
elif line_orientation == 1:
    while i < num_char:
        print(type_char)
        i += 1
