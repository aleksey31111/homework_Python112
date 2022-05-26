def add_action_title(action_title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {action_title}".center(40, '+'))
            output = func(*args, **kwargs)
            print("+ " * 25)
            return output
        return wrap
    return wrapper


class UserInterface:
    @add_action_title("Ввод данных о фильме")
    def wait_user_answer(self):
        print("Действие с фильмами:")
        print("1 - Добавление фильма"
              "\n2 - Каталог фильма"
              "\n3 - Просмотр определенного фильма"
              "\n4 - Удаление фильма"
              "\nq - Выход из программы")
        user_answer = input("Выберите вариант действия: ")

