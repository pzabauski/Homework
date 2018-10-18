# Пользователь вводит строку. Проверить является ли эта строка палиндромом.


# Решение 1
a = input('Введите строку')

if a[0:int(len(a)/2+1)] == a[-1:-int(len(a)/2+2):-1]:
    print('palyndrome')
else:
    print('not a palyndrome')

# Решение 2:
a = input('Введите строку')
if a == a[::-1]:
    print('palyndrome')
else:
    print('not a palyndrome')
