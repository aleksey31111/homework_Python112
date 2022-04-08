### Task 1 ###
print("Задание 1: Реализуйте класс <<Книга>>.\n"
      "Необходимо хранить в полях класса: Название книги, Год выпуска, Издателя, Жанр, Автора, Цену.\n"
      "1 - Реализуйте Методы Класса для Ввода Данных.\n"
      "2 - Вывода Данных.\n"
      "3 - Реализуйте доступ к Отдельным Полям через Методы Класса.")
print()


class Book:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, book_title, year_of_issue, publisher, genre, author, price):
       self.book_title = book_title
       self.year_of_issue = year_of_issue
       self.publisher = publisher
       self.genre = genre
       self.author = author
       self.price = price

    def get_book_info(self):
        print(f"Название книги: {self.book_title}\n"
              f"Год выпуска: {self.year_of_issue}\n"
              f"Издатель: {self.publisher}\n"
              f"Жанр: {self.genre}\n"
              f"Автор: {self.author}\n"
              f"Цена: {self.price}")

    def set_book_info(self, title, release, publisher, genre, author, price):
        self.book_title = title
        self.year_of_issue = release
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def get_book_title(self):
        return self.book_title

    def set_book_title(self, book_title):
        self.book_title = book_title

    def get_year_of_issue(self):
        return self.year_of_issue

    def set_year_of_issue(self, year_of_issue):
        self.year_of_issue = year_of_issue

    def get_publisher(self):
        return self.publisher

    def set_publisher(self, publisher):
        self.publisher = publisher

    def get_genre(self):
        return self.genre

    def set_genre(self, genre):
        self.genre = genre

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

book1 = Book("Злая река", 2010, "Азбука-Артикус", "Детектив", "Линколтн Чайлд, Дуглас Престон", 1000)
book1.get_book_info()
print()
book1.set_book_info("Старые кости", 2008, "Литрес", "Детектив", "Линкольн Чайлд, Дуглас Престон", 500)
book1.get_book_info()
print()
book1.set_book_title("Баязет")
print(book1.get_book_title())
book1.set_year_of_issue(1960)
print(book1.get_year_of_issue())
book1.set_publisher("Издательский Дом Вече")
print(book1.get_publisher())
book1.set_genre("Роман")
print(book1.get_genre())
book1.set_author("Валентин Пикуль")
print(book1.get_author())
book1.set_price("2000")
print(book1.get_price())