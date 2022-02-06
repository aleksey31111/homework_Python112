# start = int(input("Введите начало диапазона: "))
# end = int(input("Введите конец диапазона: "))
# end_1 = end + 1 # Увеличиваем цифру конца диапазона на 1
# end_2 = end + 2 # Увеличиваем цифру конца диапазона на 2
# end_3 = end + 2 # Увеличиваем цифру конца диапазона на 3
# start_1 = start + 1 # Увеличиваем цифру начало диапазона на еденицу
# range(start, end)
# if start % 2 != 0 & end % 2 == 0: # Если начало нечетное И конец четное.
#     for odd_namber in (range(start, end, 2)): # Перечисление диапазона с шагом 2
#         print(odd_namber, end=" ") # Вывод
# elif start % 2 == 0 & end % 2 != 0: # Иначе начало четное И конец нечетное
#     for odd_namber in range(start, end_3, 2):
#         print(odd_namber, end=" ")
# elif start % 2 != 0 & end % 2 != 0:
#     for odd_namber in range(start, end_1, 2):
#         print(odd_namber, end=" ")
# elif start % 2 == 0 & end % 2 == 0:
#     for odd_namber in range(start_1, end, 2):
#         print(odd_namber, end=" ")
##### В ЭТОМ КОДЕ НЕ УЧИТЫВАЕТСЯ ПОСЛЕДНЕЕ ( если нечетное ) ЧИСЛО ПРИ ВЫВОДЕ ######

start = input("Введите начало диапазона: ")
while type(start) != int:
    try:
        start = int(start)
    except ValueError:
        print("Число не целое!")
        start = input("Введите целое число: ")
end = input("Введите конец диапазона: ")
while type(end) != int:
    try:
        end = int(end)
    except ValueError:
        print("Число не целое!")
        end = input("Введите целое число: ")
end_1 = end + 1
for odd_namber in range(start, end + 1):
    if odd_namber % 2 != 0:
        print(odd_namber, end=" ")
