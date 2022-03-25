### Term 1 ###
print("Задание 1: Найти Введенное Пользователем Значение в 5 Списке, n\ \
      Отсортированным по Возрастанию или Убыванию по Выбору Пользователя,n\ \
      Составленным Из 4-х Списков.")
list1 = [5, 9, 6, 7]
list2 = [3, 11, 8]
list3 = [2, 4]
list4 = [10, 1, 12]
list5 = list1 + list2 + list3 + list4



def bubble_sorted_increment(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]





def binary_search_increment(s, item):
    first = 0
    last = len(s) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if s[midpoint] == item:
            found = True
        else:
            if item < s[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    # return found
    if found:
        print(f"Значене {search_in_bubble_sorted_increment} найдено")
    else:
        print(f"Значене {search_in_bubble_sorted_increment} не найдено")


def bubble_sorted_decrement(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


def line_search_decrement(s, item):
    pos = 0
    found = False
    while pos < len(s) and not found:
        if s[pos] == item:
            found = True
        else:
            pos = pos + 1
    # return found
    if found:
        print(f"Значене {search_in_bubble_sorted_decrement} найдено")
    else:
        print(f"Значене {search_in_bubble_sorted_decrement} не найдено")


# print(line_search_decrement(list5, 12))

inp = int(input("1 - Сортировка по убыванию\n2 - Сортировка по Возрастанию\n ->"))
if inp == 1:
    bubble_sorted_decrement(list5)
    print(list5)
    search_in_bubble_sorted_decrement = int(input("Введите значение для поиска: "))
    line_search_decrement(list5, search_in_bubble_sorted_decrement)
elif inp == 2:
    bubble_sorted_increment(list5)
    print(list5)
    search_in_bubble_sorted_increment = int(input("Введите значение для поиска: "))
    binary_search_increment(list5, search_in_bubble_sorted_increment)
