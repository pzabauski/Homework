def print_field(field):
    print('   ''| 1 | 2 | 3 |')
    print('---''+---+---+---+')
    print(' 1 ''| %s |' % ' | '.join(field[0]))
    print('---''+---+---+---+')
    print(' 2 ''| %s |' % ' | '.join(field[1]))
    print('---''+---+---+---+')
    print(' 3 ''| %s |' % ' | '.join(field[2]))
    print('---''+---+---+---+')