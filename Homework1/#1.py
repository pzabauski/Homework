# Пользователь вводит целое число. Найти наибольшую и наименьшую цифру в числе.



x = input('Введите целое число')

# Решение 1
print(max(x))
print(min(x))

# Решение 2
# наибольшее число
if x.__contains__(str(9)):
    print('Наибольшее число 9')
elif x.__contains__(str(8)):
    print('Наибольшее число 8')
elif x.__contains__(str(7)):
    print('Наибольшее число 7')
elif x.__contains__(str(6)):
    print('Наибольшее число 6')
elif x.__contains__(str(5)):
    print('Наибольшее число 5')
elif x.__contains__(str(4)):
    print('Наибольшее число 4')
elif x.__contains__(str(3)):
    print('Наибольшее число 3')
elif x.__contains__(str(2)):
    print('Наибольшее число 2')
else:
    print('Наибольшее число 1')

# Наименьшее число
if x.__contains__(str(1)):
    print('Наименьшее число 1')
elif x.__contains__(str(2)):
    print('Наименьшее число 2')
elif x.__contains__(str(3)):
    print('Наименьшее число 3')
elif x.__contains__(str(4)):
    print('Наименьшее число 4')
elif x.__contains__(str(5)):
    print('Наименьшее число 5')
elif x.__contains__(str(6)):
    print('Наименьшее число 6')
elif x.__contains__(str(7)):
    print('Наименьшее число 7')
elif x.__contains__(str(8)):
    print('Наименьшее число 8')
else:
    print('Наименьшее число 9')

