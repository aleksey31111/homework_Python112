### Term 1 ###
print("Задание 1: Создать два словаря из одного, в 1: Имя и Зарплата, во 2: Удалить Имя и Зарплату")
employee = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
employee_name_salary = dict()
for i in employee.items():
    if i[0] == 'name' and i[1] == 'Kelly':
        employee_name_salary[i[0]] = i[1]
    elif i[0] == 'salary' and i[1] == 8000:
        employee_name_salary[i[0]] = i[1]
del employee['name']
del employee['salary']
print(employee)
print(employee_name_salary)
print()
print()

### Term 2 ###
print("Задание 2: Переименовать Ключ city в location, в типе данных Словарь")
employee = {'Name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
employee.pop('city')  # = 'location'
employee['location'] = 'New York'
print(employee)
