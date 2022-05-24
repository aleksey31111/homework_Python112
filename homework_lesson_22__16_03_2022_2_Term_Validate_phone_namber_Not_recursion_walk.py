### Term 1 ###
import re

print("Задание 1: Валидация НОМЕРА ТЕЛЕФОНА.\n \
 +7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 7 (499) 456-45-78")
phone_numer = "+7 499 456-45-78 ,2222222, 222222, 7 566 22 22, +74994564578, 7 (499) 456 45 78, 7 (499) 456-45-78"
# pat = r'[+]\s?[7]\s?([\d{3}]){2}\-([\d{2}]){2}'
# pat = r"([+]\s?[\d]+\s[\d]+\s[\d]+\s[\d])|([+][\d]+)"  # True 2
# pat = r"[+7]\s(:?[\d{3}])\s?(:?[\d{3}])-?(:?[\d{2}])-?(:?[\d]{2})  #|(:?[+][\d]+)"
# pat = r'^\+7\s[\d{3}]\s[\d{3}]\-[\d{2}]\-[\d{2}]$'  #|[7]\s[(499)]\s[456]\s[45]\s[78]'
pat = r'\+7\s\d{3}\s\d{3}-\d{2}-\d{2}|[+7]\d{11}|[7]\s\(\d{3}\)\s\d{3}\s?-?\d{2}\s?-?\d{2}'
print(re.findall(pat, phone_numer))


### Term 2 ###
def walk_list(lst1):
    lst = []
    i = 0
    while len(lst1) != 10:
        if not isinstance(lst1[i], list):
            lst.append(lst1[i])
        i += 1
    return lst



names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
print("Выпрямленный СПИСОК: ", walk_list(names))
