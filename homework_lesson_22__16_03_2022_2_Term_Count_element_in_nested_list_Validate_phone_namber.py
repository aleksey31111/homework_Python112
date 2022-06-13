### Term 1 ###
import re

print("Задание 1: Валидация НОМЕРА ТЕЛЕФОНА.\n \
 +7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 7 (499) 456-45-78")
phone_numer = "+7 499 456-45-78 , +74994564578, 7 (499) 456 45 78, 7 (499) 456-45-78"
pat = r'\+7\s\d{3}\s\d{3}-\d{2}-\d{2}|[+7]\d{11}|[7]\s\(\d{3}\)\s\d{3}\s?-?\d{2}\s?-?\d{2}'
print(re.findall(pat, phone_numer))


### Term 2 ###
print("Задание 2: Посчитать количество Элементов во ВЛОЖЕННОМ СПИСКЕ,\n \
      Не Используя РЕКУРСИЮ.")

names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']

count = 0
for el_list in names:
    if isinstance(el_list, list):
        print(f"el_list: {el_list}")
        for el_list1 in el_list:
            if isinstance(el_list1, list):
                print(f"el_list1: {el_list1}")
                for el_list2 in el_list1:
                    if isinstance(el_list2, list):
                        print(f"el_list2: {el_list}")
                    elif not isinstance(el_list2, list):
                        count += 1
            elif not isinstance(el_list1, list):
                count += 1
    elif not isinstance(el_list, list):
        count += 1
print(count)

