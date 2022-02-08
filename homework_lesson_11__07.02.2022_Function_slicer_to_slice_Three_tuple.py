from random import randint

### Term 1 ###
print("Задание 1: Функция slicer() с tuple и round(random * 100)."
      "Вернуть: slice[elem:elem] или slice[elem:] или tuple()")


# t = tuple(round(random * 100) for i in range(round(random * 10)))
# t = (int(input("-->"))) # for i in range(1, 3))

# t = tuple(randint(0, 100) for i in range(1, 10))

def slicer(t, num):
    # return t.index(num, 0, -1)
    # return t.index(num, t.index(num)+1, -1)
    # iter = 0
    # for i in t:
    for num in t:
        if t.index(num, 0, -1):
            return t.index(num, 0, -1)
        # one_meet = t.index(num)
        #     if t.index(num, t.index(num), -1):
        #         return t[t.index(num, 0, -1): t.index(num, t.index(num, 0, -1) + 1, -1)]
        #     else:
        #         return (t[t.index(num):])
        else:
            return tuple()
    else:
        return tuple()
        # iter += 1
        # s = tuple(round(random * 100) for i in range(round(random * 10)))


print(slicer((1, 2, 3), 8))
print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(slicer((1, 2, 8, 5, 1, 2, 9), 8))


### Term 2 ###
print("Задание 2: 1 - кортеж от 0 до 5, 2 - кортеж от -5 до 0. Одну функцию для заполнения кортежей."
      "Обьединить кортеж с помощью операции + в Кортеж 3. С помощью метода кортежа count() определить количество 0 в 3 Кортеже"
      "Вывести 3 Кортеж и Количество 0")