### Term 1 ###
print("Задание 1: Посчитать количество Элементов во ВЛОЖЕННОМ СПИСКЕ,\n \
      Не Используя РЕКУРСИЮ.")
names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']

count = 0
# print(len(names))
for element in names:
    if len(element[0]) < 2 and element[0].isupper():
        # print(element)
        count += 1
    else:
        for element1 in element:
            if len(element1[0]) < 2 and element1[0].isupper():
                # print(element1)
                count += 1
            else:
                for element2 in element1:
                    if len(element2[0]) < 2 and element2[0].isupper():
                        # print(element2)
                        count += 1
print()
print(f"Количество Елементов в Списке: {count}")
print()

### Term 2 ###
import re

print("Задание 2: Валидация НОМЕРА ТЕЛЕФОНА.\n \
 +7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 7 (499) 456-45-78")
phone_numer = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 7 (499) 456-45-78"
pat = r''
print(re.findall(pat, phone_numer))
