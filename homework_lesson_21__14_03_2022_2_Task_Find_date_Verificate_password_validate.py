import re

### Task 1: ###
print("Задание 1: Найти ДАТУ в Формате: dd/mm/YYYY")
print()
print("Variant 1: Usually search throuch 're.findall(pat, string)'.")
weather_string = "В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, были зафиксированны максимумы ежемесячных осадков."
pat = r'[\d]{2}/[\d]{2}/[\d]{4}'
print(re.findall(pat, weather_string))
print()
print("Variant 2: Function.")


def date_of_weather_anomaly(news_string):
    return re.findall(r'[\d]{2}/[\d]{2}/[\d]{4}', news_string)


print(date_of_weather_anomaly(weather_string))
print()
### Task 2: ###
print("Задание 2: Проверка Соответствия ПАРОЛЯ.\n \
      ПАРОЛЬ Должен Состоять Из ЦИФР, БУКВ Английского Алфавита,\n \
      Символов ДЕФИС, СОБАКА и ПОДЧЕРКИВАНИЕ. Длина ПАРОЛЯ от 6 до 18 символов.")
print()


def varificate_password(string_password):
    # return re.findall(r'^[a-z0-9@_-]{6,18}$', string_password, re.I)
    # return re.findall(r'^[\w+[!#$%^&*()+]?@_-]{6,17}$', string_password, re.I)
    return re.findall(r'^[\w@_-]{6,18}$', string_password, re.I)


print(varificate_password('my-p@ssw0rd'))
