from pole_chudes.custom_exceptions import GameOver
from pole_chudes.data_reader import CSVGetter
from pole_chudes.game_process import GameProcess


def play():
    data_reader = CSVGetter('pole_chudes/words.csv')
    game = GameProcess(data_reader)
    game.play()


if __name__ == '__main__':
    while True:
        try:
            play()
        except GameOver as err:
            print(f'You completed {err.score} words')
            y = input('Enter: Y if you want to continue')
            if y.lower() != 'y':
                break
