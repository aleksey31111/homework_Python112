from random import randint

### Term 1 ###
print("Задание 1: Функция slicer() с tuple.\n"
      "Вернуть: slice[elem:elem] или slice[elem:] или tuple()")


def slicer(t, num):
    if num in t:
        if t.count(num) == 1:
            return t[t.index(num, 0, -1)::]
        elif t.count(num) > 1:
            # f = t.index(num)
            # s = t.index(num, f + 1)
            return t[t.index(num, 0, -1): t.index(num, t.index(num) + 1) + 1:]
    else:
        return tuple()


print(slicer((1, 2, 3), 8))
print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(slicer((1, 2, 8, 5, 1, 2, 9), 8))
print()
print()

### Term 2 ###
print("Задание 2: 1 - кортеж от 0 до 5, 2 - кортеж от -5 до 0. Одну функцию для заполнения кортежей."
      "Обьединить кортеж с помощью операции + в Кортеж 3. С помощью метода кортежа count() определить количество 0 в 3 Кортеже"
      "Вывести 3 Кортеж и Количество 0")

t1 = [randint(0, 5) for i in range(10)]
t2 = [randint(-5, 0) for i in range(10)]
# t1 = tuple(s1)
# t2 = tuple(s2)
t3 = t1 + t2
print(t3)
print(t3.count(0))
