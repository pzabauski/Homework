from initial import data
from initial import temp_data
import sys

checklist = ['11', '12', '13', '21', '22', '23', '31', '32', '33']

def player1_turn():
    player1_input = input('Игрок 1: Введите координаты')
    if player1_input in checklist:
        pass
    else:
        print('Неверно введены координаты')
        sys.exit('Начните заново')                                      # Как можно отсюда вернуться к input ? чтобы не прекращать программу каждый раз когда юзер сделал неправильный ввод
    temp_data[int(player1_input[0]) - 1][int(player1_input[1]) - 1] = 'x'
    return


def player2_turn():
    player2_input = input('Игрок 2: Введите координаты')
    if player2_input in checklist:
        pass
    else:
        print('Неверно введены координаты')
        sys.exit('Начните заново')
    temp_data[int(player2_input[0]) - 1][int(player2_input[1]) - 1] = '0'
    return














