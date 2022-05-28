import pickle
import os.path


class Movie:
    def __init__(self, title, genre, director, years, duration, studio, actors):
        self.title = title
        self.genre = genre
        self.director = director
        self.years = years
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f'{self.title} - {self.years} ({self.director})'


class MovieModel:
    def __init__(self):
        self.db_name = 'homework_38_moviecontainer.txt'
        self.movies = self.load_data()

    def add_movie(self, dict_movie):
        movie = Movie(*dict_movie.values())
        self.movies[movie.title] = movie

    def get_all_movies(self):
        return self.movies.values()

    def get_single_movie(self, user_title):
        movie = self.movies[user_title]
        dict_movie = {
            "Название фильма": movie.title,
            "Жанр": movie.genre,
            "Режиссер": movie.director,
            "Год выпуска": movie.years,
            "Длительность": movie.duration,
            "Студия": movie.studio,
            "Актеры": movie.actors
        }
        return dict_movie

    def remove_movie(self, user_title):
        return self.movies.pop(user_title)

    def save_data(self):
        with open(self.db_name, 'wb') as hw_38:
            pickle.dump(self.movies, hw_38)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, 'rb') as hw_38:
                return pickle.load(hw_38)
        else:
            return dict()
