### Term 1 ###
print("Задание 1: Посчитать количество Элементов во ВЛОЖЕННОМ СПИСКЕ,\n \
      Не Используя РЕКУРСИЮ.")
### Variant 1 ###
names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']

count = 0
# print(len(names))
for element in names:
    if len(element[0]) < 2 and element[0].isupper():
        print(element, end=" ")
        count += 1
    else:
        for element1 in element:
            if len(element1[0]) < 2 and element1[0].isupper():
                print(element1, end=" ")
                count += 1
            else:
                for element2 in element1:
                    if len(element2[0]) < 2 and element2[0].isupper():
                        print(element2, end=" ")
                        count += 1
print()
print(f"Количество Елементов в Списке: {count}")
print()
### Variant 2 ###
print("Выпрямление СПИСКА с Использованием Рекурсии:")


def union(s):
    if not s:  # s == []:
        return s
    if isinstance(s[0], list):
        return union(s[0]) + union(s[1:])
    return s[:1] + union(s[1:])


names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
print("Выпрямленный СПИСОК: ", union(names))

### Term 2 ###
import re

print("Задание 2: Валидация НОМЕРА ТЕЛЕФОНА.\n \
 +7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 7 (499) 456-45-78")
phone_numer = "+7 499 456-45-78 , +74994564578, 7 (499) 456 45 78, 7 (499) 456-45-78"
# pat = r'[+]\s?[7]\s?([\d{3}]){2}\-([\d{2}]){2}'
# pat = r"([+]\s?[\d]+\s[\d]+\s[\d]+\s[\d])|([+][\d]+)"  # True 2
# pat = r"[+7]\s(:?[\d{3}])\s?(:?[\d{3}])-?(:?[\d{2}])-?(:?[\d]{2})  #|(:?[+][\d]+)"
# pat = r'^\+7\s[\d{3}]\s[\d{3}]\-[\d{2}]\-[\d{2}]$'  #|[7]\s[(499)]\s[456]\s[45]\s[78]'
pat = r'\+7\s\d{3}\s\d{3}-\d{2}-\d{2}|[+7]\d{11}|[7]\s\(\d{3}\)\s\d{3}\s?-?\d{2}\s?-?\d{2}'
print(re.findall(pat, phone_numer))
