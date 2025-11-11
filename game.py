from random import randint
from class_game import Game
from constants import ADMIN_USERNAME, UNKNOWN_COMMAND


def game(game_obj):
    number = randint(1, 100)
    print(
        "\nУгадайте число от 1 до 100.\n"
        'Для выхода из текущей игры введите команду "stop"'
    )

    while True:
        user_input = input("Введите команду или число: ").strip().lower()

        match user_input:
            case "stop":
                break
            case "stat":
                game_obj.get_statistics(username=game_obj.username)
            case "answer":
                game_obj.get_right_answer(number,username=game_obj.username)
            case _:
                try:
                    guess = int(user_input)
                except ValueError:
                    print(UNKNOWN_COMMAND)
                    continue

                if game_obj.check_number(guess, number):
                    break


def get_username() -> str:
    username = input("Представьтесь, пожалуйста, как Вас зовут: ")
    if username == ADMIN_USERNAME:
        print(
            "\nДобро пожаловать, создатель! "
            'Во время игры вам доступны команды "stat", "answer"'
        )
    else:
        print(f"{username}, добро пожаловать в игру!")
    return username


def guess_number() -> None:
    username = get_username()
    game_obj = Game(username)
    while True:
        game_obj.total_games += 1
        game(game_obj)
        play_again = input("Хотите сыграть еще? (yes/no): ").strip().lower()
        if play_again not in ("y", "yes"):
            break


if __name__ == "__main__":
    print('Вас приветствует игра "Угадай число"\nДля выхода нажмите Ctrl+C')
    guess_number()
