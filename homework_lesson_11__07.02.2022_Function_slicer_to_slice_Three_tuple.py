from random import randint

### Term 1 ###
print("Задание 1: Функция slicer() с tuple и round(random * 100)."
      "Вернуть: slice[elem:elem] или slice[elem:] или tuple()")


# t = tuple(round(random * 100) for i in range(round(random * 10)))
# t = (int(input("-->"))) # for i in range(1, 3))

# t = tuple(randint(0, 100) for i in range(1, 10))

# def slicer(t, num):
#     # return t.index(num, 0, -1)
#     # return t.index(num, t.index(num)+1, -1)
#     # iter = 0
#     # for i in t:
#     for num in t:
#         if t.index(num, 0, -1):
#             return t.index(num, 0, -1)
#         # one_meet = t.index(num)
#         #     if t.index(num, t.index(num), -1):
#         #         return t[t.index(num, 0, -1): t.index(num, t.index(num, 0, -1) + 1, -1)]
#         #     else:
#         #         return (t[t.index(num):])
#         else:
#             return tuple()
#     else:
#         return tuple()
#         # iter += 1
#         # s = tuple(round(random * 100) for i in range(round(random * 10)))
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))
t = ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 8, 12))
num = 8
for i in t:
    if t.index(num):
        first = t.index(num)
        second = t[t.index(num, 0) + 1::]
        third = t[-1:t.index(num):-1]
        forth = t[t.index(num) + 1:t.index(num)]
        fivth = t.index(num, t.index(num) + 1, -1)
        if t.index(num) and t.index(num, t.index(num) + 1, -1):
            print(t[t.index(num, num + 1, -1): t.index(num, num + 1, -1)])

print(first, end=" ")
print()
print(second, end=" ")
print()
print(third, end=" ")
print()
print(forth, end=" ")
print()
print(fivth, end=" ")

print()
print()

### Term 2 ###
print("Задание 2: 1 - кортеж от 0 до 5, 2 - кортеж от -5 до 0. Одну функцию для заполнения кортежей."
      "Обьединить кортеж с помощью операции + в Кортеж 3. С помощью метода кортежа count() определить количество 0 в 3 Кортеже"
      "Вывести 3 Кортеж и Количество 0")


s1 = [randint(0, 5) for i in range(10)]
s2 = [randint(-5, 0) for i in range(10)]
t1 = tuple(s1)
t2 = tuple(s2)
print(type(t1))
print(type(t2))
print(t1, end=" ")
print(t2, end=" ")
t3 = t1 + t2
print(t3)
# for i in t3:
print(t3.count(0))
