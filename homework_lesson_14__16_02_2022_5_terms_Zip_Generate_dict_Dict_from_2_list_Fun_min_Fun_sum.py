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
### Term 4 ###
print("Задание 4: Создать функцию минимального числа, произвольного количесива чисел")


# nambers = (10,9)
def minimal_namber(*args):
    # return (args)
    # nambers = list(args)
    return min(args)


print(minimal_namber(10, 9))
print(minimal_namber(2, 3, 4))
print(minimal_namber(3, 5, 10, 6))

### Term 5 ###
print("Задание 5: Найти сумму элементов, предыдущего значения с текущим, произвольного количества Элементов. ")


def sum_nambers(*args):
    # print(len(args))
    nambers = list()
    length = len(args)
    itr = iter(args)
    # if len(args) == 1:
    #     a = next(itr)
    a = next(itr)
    nambers.append(a)
    # while length < 0:
    #     b =
    nambers.append(a + next(itr))
    # nambers.append(a + next(itr))
    # nambers.append(a + next(itr))
    # nambers.append(a + next(itr))
    # nambers.append(a + next(itr))
    # length -= 1
    # for i in len(args):
    #     if len(args) ==1:
    #         a = next(itr)
    #         args.append(a)
    #     elif len(args) > 1:
    #         b = a + next(itr)
    #         args.append(b)
    return nambers


print(sum_nambers(3, 9, 1))
print(sum_nambers(2, 5, 4, 2))
print(sum_nambers(3, 5, 10, 6, 3))
