from initial import data
import sys


def check_rows():
    win_data1 = [['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']]
    win_data2 = [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
    for i in range(0, 3):
        if data[i] == win_data1[i]:
            print('Player_1 wins')
            sys.exit()
        elif data[i] == win_data2[i]:
            print('Player 2 wins')
            sys.exit()
        else:
            continue


def check_columns():
    for i in range(0, 3):
            if data[0][i] == 'x' and data[1][i] == 'x' and data[2][i] == 'x':
                print('Player1 wins')
                sys.exit()
            elif data[0][i] == '0' and data[1][i] == '0' and data[2][i] == '0':
                print('Player2 wins')
                sys.exit()
            else:
                continue


def check_diagonals():
    for i in range(0, 3):
        if data[0][0] == 'x' and data[1][1] == 'x' and data[2][2] == 'x':
            print('Player1 wins')
            sys.exit()
        elif data[0][2] == 'x' and data[1][1] == 'x' and data[2][0] == 'x':
            print('Player1 wins')
            sys.exit()
        elif data[0][2] == '0' and data[1][1] == '0' and data[2][0] == '0':
            print('Player2 wins')
            sys.exit()
        elif data[0][0] == '0' and data[1][1] == '0' and data[2][2] == '0':
            print('Player2 wins')
            sys.exit()
        else:
            continue

