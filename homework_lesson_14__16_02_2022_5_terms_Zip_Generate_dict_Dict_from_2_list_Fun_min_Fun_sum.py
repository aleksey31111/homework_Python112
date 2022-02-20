### Term 1 ###
print("Задание 1: Словарь из Двух Списков Одинаковой Длинны, 1 - Ключ, 2 - значение.")
color = ['red', 'green', 'blue']
hex_value = ['#FF0000', '#008000', '#0000FF']
dict_hex_value = dict(zip(color, hex_value))
print(dict_hex_value)
print()
print()

### Term 2 ###
print("Задание 2: Создать словарь из 9 Элементов key = key**3.")
dict_val_mul_three = {i: pow(i, 3) for i in range(1, 10)}
print(dict_val_mul_three)
print()
print()

### Term 3 ###
print("Задание 3: Из 2 Списков Данных Создать Новый Словарь Используя Генратор Словарей. ")
suit_keys = ['color', 'fruit', 'pet']
suit_values = ['blue', 'apple', 'dog']
print(dict(zip(suit_keys, suit_values)))
print()
print()
### Term 4 ###
print("Задание 4: Создать функцию минимального числа, произвольного количесива чисел")


# nambers = (10,9)
def minimal_namber(*args):
    # return (args)
    # nambers = list(args)
    return min(args)


for i in (10, 9):
    print(i, end=" ")
print()
for i in (2, 3, 4):
    print(i, end=" ")
print()
for i in (3, 5, 10, 6):
    print(i, end=" ")
print()
print()
print(minimal_namber(10, 9))
print(minimal_namber(2, 3, 4))
print(minimal_namber(3, 5, 10, 6))
print()
print()
### Term 5 ###
print("Задание 5: Найти сумму элементов, предыдущего значения с текущим, произвольного количества Элементов. ")


## First Variant without Cicle ##

def sum_nambers(*args):
    nambers = list()
    itr = iter(args)
    a = next(itr)  # 1
    nambers.append(a)
    b = a + next(itr)  # 2
    nambers.append(b)
    c = b + next(itr, "STOP")  # 3
    nambers.append(c)
    if len(args) > 3:
        d = c + next(itr, "STOP")  # 4
        nambers.append(d)
        if len(args) > 4:
            e = d + next(itr, "STOP")
            nambers.append(e)
    return nambers


for i in [3, 9, 1]:
    print(i, end=" ")
print()
for i in [2, 5, 4, 2]:
    print(i, end=" ")
print()
for i in [3, 5, 10, 6, 3]:
    print(i, end=" ")
print()
print()
for i in sum_nambers(3, 9, 1):
    print(i, end=" ")
print()
for i in sum_nambers(2, 5, 4, 2):
    print(i, end=" ")
print()
for i in sum_nambers(3, 5, 10, 6, 3):
    print(i, end=" ")
# print(sum_nambers(3, 9, 1))
# print(sum_nambers(2, 5, 4, 2))
# print(sum_nambers(3, 5, 10, 6, 3))

# ## Second Variant Via while ## NOT WORKING
# def sum_nambers(*args):
#     print(len(args))
#     nambers = list()
#     length = len(args)
#     while length == length:
#         # itr = iter(args)
#         nambers.append(next(iter(args)))
#         length -= 1
#     while length != length and length > 0:
#         nambers.append(args[0] + next(iter(args)))
#         length -= 1
#         return nambers
#
#
# print(sum_nambers(3, 9, 1))
# print(sum_nambers(2, 5, 4, 2))
# print(sum_nambers(3, 5, 10, 6, 3))
