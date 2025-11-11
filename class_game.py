from datetime import datetime as dt
from constants import ADMIN_USERNAME, UNKNOWN_COMMAND
from access_control import access_control

class Game:
    def __init__(self, username: str):
        self.username = username
        self.total_games = 0
        self.start_time = dt.now()


    @access_control
    def get_statistics(self, *args, **kwargs) -> None:
        game_time = dt.now() - self.start_time
        print(f"Общее время игры: {game_time}, текущая игра - №{self.total_games}")


    @staticmethod
    @access_control
    def get_right_answer(number,*args, **kwargs) -> None:
        print(f"Правильный ответ: {number}")


    def check_number(self, guess: int, number: int) -> bool:
        if guess == number:
            print(f"Отличная интуиция, {self.username}! Вы угадали число :)")
            return True

        if guess < number:
            print("Ваше число меньше загаданного")
        else:
            print("Ваше число больше загаданного")

        return False
