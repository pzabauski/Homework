from print_field import print_field       # Не могу понять почему подчеркивается?
from initial import data
from initial import temp_data
from make_turn import player1_turn, player2_turn
from check_field import check_field
from check_range import check_rows, check_diagonals, check_columns



def player1():
    player1_turn()
    check_field()
    check_rows()
    check_columns()
    check_diagonals()
    print_field(data)


def player2():
    player2_turn()
    check_field()
    check_rows()
    check_columns()
    check_diagonals()
    print_field(data)


for i in range(1, 5):
    if i == 5:
        print('Ходы закончились - ничья')
    else:
        print('Ход № %d' % i)
        player1()
        player2()
