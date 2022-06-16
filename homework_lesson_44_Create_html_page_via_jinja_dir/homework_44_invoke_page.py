from jinja2 import Template, Environment, FileSystemLoader

print("Homework 44 Invoke Page")

homework = ["Страница с домашним заданием", "Домашнее задание выполненно"]

file_loader = FileSystemLoader('')
env = Environment(loader=file_loader)
tm = env.get_template('main_homework_44_of_page.html')
msg = tm.render(title="Домашнее задание")

print(msg)