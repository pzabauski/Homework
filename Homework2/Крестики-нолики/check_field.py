from initial import data
from initial import temp_data
import sys
from make_turn import player1_turn
from make_turn import player2_turn
from print_field import print_field

def check_field():
    for i in range(0, 3):
        for j in range(0, 3):
            if temp_data[i][j] == ' ':
                pass
            elif temp_data[i][j] != ' ':
                if data[i][j] != ' ':
                    print('Данные координаты уже заняты')
                    temp_data[i][j] = ' '
                    sys.exit('Начните заново')
                else:
                    data[i][j] = temp_data[i][j]
                    temp_data[i][j] = ' '
            else:
                print('Неверно введены координаты')
                sys.exit('Начните заново')









