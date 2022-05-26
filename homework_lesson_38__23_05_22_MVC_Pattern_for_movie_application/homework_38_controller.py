# from  homework_38_view import UserInterface
# from homework_38_model import MovieModel

class Controller:
    def __init__(self):
        self.movie_model = ''
        self.user_interface = ''

    def run(self):
        answer = None
        while answer != 'q':
            answer = self.user_interface.wait_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer == '1':