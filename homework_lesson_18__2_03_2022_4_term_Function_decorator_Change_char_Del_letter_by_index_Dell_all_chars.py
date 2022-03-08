### Term 1: ###
print("Задание 1: "
      "Создать ФУНКЦИЮб которая будет Находить СУММУ любого количества ЧИСЕЛ и"
      "ДЕКОРАТОРБ который будет находить СРЕДНЕЕ АРИФМЕТИЧЕСКОЕ Этих ЧИСЕЛ.")


def decor_average(*args):
    def wrapper(func):
        def wrap(*f_args):
            sum_nam = sum(f_args)
            average_nam = sum_nam / len(args)
            print("Сумма чисел", *f_args, "=", sum_nam)
            print("Среднее аривметическое чисел", *args, "=", average_nam)

        return wrap

    return wrapper


@decor_average(2, 3, 3, 4)
def func_sum(*f_args):
    print("Сумма чисел" "Среднее арифметическое")


print(func_sum(2, 3, 3, 4))
print()
print()
### Term 2: ###
print("Задание 2: Замена СИМВОЛА на ДРУГОЙ СИМВОЛ в СТРОКЕ на ЧЕТНЫХ ПОЗИЦИЯХ.")


def change_char_even_index(s, new, old):
    buffer_str_1 = ""
    char = 0
    while char < len(s):
        if char % 2 == 0 and s[char] == old:
            buffer_str_1 += new
        else:
            buffer_str_1 += s[char]
        char += 1

    return buffer_str_1


str1 = "Я изучаю Nython. Мне очень нравится Nython. Nython очень интерестный язык программирования."
str2 = change_char_even_index(str1, 'P', 'N')
print("str1 = " + str1)
print("str2 = " + str2)
print()
print()

### Term 3: ###
print("Задание 3: Удаление БУКВЫ из СЛОВА, Заданной НОМЕРОМ ПОЗИЦИИ.")


def del_char(s, simbol):
    buffer_s = ""
    for char in range(len(s)):
        if char != simbol:
            buffer_s += s[char]
    return buffer_s


str1 = "0123456789"
str2 = del_char(str1, 4)
print("s = " + str1)
print("s2 = " + str2)
print()
print()

### Task 4 ###
print("Задание 4: Удаление ВСЕХ ВХОЖДЕНИЙ заданного СИМВОЛА из СТРОКИ.")


def dell_all_occurrences_char(s, characters):
    buffer_s = ""
    char = 0
    len_s = len(s)
    for char in s:
        if char != characters:
            buffer_s += char
    return buffer_s


str_1 = "012345363738494"
str_2 = dell_all_occurrences_char(str_1, "3")
print("s = " + str_1)
print("s2 = " + str_2)
