from func import *

import random

input1 = int(input('Введите целое число'))
numbers = []

for i in range(0, input1):
    numbers.append(random.randint(1, 9))

print(numbers)

input2 = input('Введите что сделать с этими числами\n'
               '1е слово: sum, multiply, join или unite\n'
               '2ое слово: negated, inverted или squared\n'
               '3ье слово: odds, evens или simples\n')

list_of_commands = input2.split()

third_word = {'odds': x_odds(numbers), 'evens': x_evens(numbers), 'simples': x_simples(numbers)}
numbers1 = third_word[list_of_commands[2]]
print('Result of %s:' % list_of_commands[2])
print(numbers1)


second_word = {'negated': x_negated(numbers1), 'inverted': x_inverted(numbers1), 'squared': x_squared(numbers1)}

numbers2 = second_word[list_of_commands[1]]
print('Result of %s:' % list_of_commands[1])
print(numbers2)

first_word = {'sum': x_sum(numbers2), 'multiply': x_multiply(numbers2), 'join': x_join(numbers2), 'unite': x_unite(numbers2)}

numbers = first_word[list_of_commands[0]]
print('Result of %s:' % list_of_commands[0])
print(numbers)
