from jinja2 import Template, Environment, FileSystemLoader

print("Homework 44 Invoke Page")
# peaple = [
#     {'name': "Евгений", 'born': 1995, 'height': 150 }
#     {'name': "Евгения", 'born': 1996, 'height': 160 }
#     {'name': "Анатолий", 'born': 1997, 'height': 170 }
#     {'name': "Анастасия", 'born': 1998, 'height': 180 }
#     {'name': "Прокопий", 'born': 1999, 'height': 190 }
# ]

homework = ["Страница с домашним заданием", "Домашнее задание выполненно"]

file_loader = FileSystemLoader('')
env = Environment(loader=file_loader)
tm = env.get_template('main_homework_44_of_page.html')
msg = tm.render(title="Домашнее задание")

print(msg)