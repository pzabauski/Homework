# Модуль math
# Пользователь вводит 3 числа.
# Определить, существует ли треугольник с такими сторонами, и если существует, найти его углы.
# Для решения задачи можно использовать теорему косинусов.

import math

A = int(input("Введите число №1"))
B = int(input("Введите число №2"))
C = int(input("Введите число №3"))


if A + B > C and B + C > A and A + C > B:
    cos_a = (A ** 2 - B ** 2 - C ** 2) / (- 2 * B * C)
    cos_b = (B ** 2 - A ** 2 - C ** 2) / (- 2 * A * C)
    cos_c = (C ** 2 - A ** 2 - B ** 2) / (- 2 * A * B)
    a = math.degrees(math.acos(cos_a))
    b = math.degrees(math.acos(cos_b))
    c = math.degrees(math.acos(cos_c))
    print("Треугольник существует")
    print('Его углы равны:')
    print('a = %f' % round(a))
    print('b = %f' % round(b))
    print('c = %f' % round(c))
else:
    print('Треугольника не существует')



