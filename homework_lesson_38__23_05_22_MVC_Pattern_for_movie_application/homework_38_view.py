def add_action_title(action_title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {action_title}".center(60, '+'))
            output = func(*args, **kwargs)
            print("+ " * 25)
            return output

        return wrap

    return wrapper


class UserInterface:
    @add_action_title("Ввод данных о фильме: ")
    def wait_user_answer(self):
        # print("Enter User Data ".center(50, '='))
        print("Действие с фильмами:")
        print("1 - Добавление информации о фильме"
              "\n2 - Каталог фильмов"
              "\n3 - Просмотр информации об определенном фильме"
              "\n4 - Удаление информации о фильме"
              "\nq - Выход из программы")
        user_answer = input("Выберите вариант действия: ")
        # print("=" * 50)
        return user_answer

    @add_action_title("Создание фильма: ")
    def add_user_movie(self):
        dict_movie = {
            "Название фильма": None,
            "Жанр": None,
            "Режиссер": None,
            "Год выпуска": None,
            "Длительность": None,
            "Студия": None,
            "Актеры": None
        }
        # print(" Creation Movie: ".center(50, "="))
        for key in dict_movie:
            dict_movie[key] = input(f"Введите {key}: ")
        # print("=" * 50)
        return dict_movie

    @add_action_title("Список фильмов: ")
    def show_all_movies(self, movies):
        # print("Lisr Movies: ".center(50, '='))
        for ind, movie in enumerate(movies, start=1):
            print(f"{ind}) {movie}")
        # print('=' * 50)

    @add_action_title("Ввод названия фильмов: ")
    def get_user_movie(self):
        user_movie = input("Введите название фильма: ")
        return user_movie

    @add_action_title("Просмотр информации о фильме: ")
    def show_single_movie(self, movie):
        for key in movie:
            print(f"{key} фильма - {movie[key]}")

    @add_action_title("Удаление фильма")
    def remove_single_movie(self, movie):
        print(f"нформация о фильме {movie} Была Удалена")

    @add_action_title("Сообщение Об Ошибке: ")
    def show_incorrect_title_error(self, user_title):
        print(f"Статьи с названием {user_title} Не Существует")

    @add_action_title("Сообщение Об Ошибке")
    def show_incorrect_answer_error(self, answer):
        print(f"Варианта с Названием {answer} Не Существует")
