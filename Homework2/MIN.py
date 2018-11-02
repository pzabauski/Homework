def min(arg, *args, key=None, **kwargs):
    if args:                                                    # Если было введено больше 1го элемента
        flag = False                                            # сигнал true или false и все вроде
        iterable = args                                         # записывает в переменную все значения которые были введены как аргументы
                                                                # потом будет перезаписывать эту переменную
        if key is None:                                         # Если в аргументах нет словарей (элементов с доступом по ключу)
            vmin, kmin = arg, arg                               # vmin и kmin - одинаковые, нет разницы
        else:                                                   # Если есть словари то kmin = значению получен. из словаря по ключу
            vmin, kmin = arg, key(arg)
    else:
        flag = True                                             # это если 1 аргумент был введен
        iterable = arg                                          # переменной iterable присвается зачения единственного аргументы
        vmin, kmin = None, None                                 # переменные vmin, kmin не существуют.

    if key is None:                                             # если в введенных аргументах НЕТ словаря создает кортеж
        iterable = map(lambda x: (x, x), iterable)              # из введенных последовательных агрументов. Создает из
    else:                                                       # переменной iterable.
        iterable = map(lambda x: (x, key(x)), iterable)         # если ЕСТЬ словарь (доступ по ключу), то делает тоже самое
                                                                # только создает кортеж в т.ч. из values добытых из словаря по ключу
    for v, k in iterable:
        if flag:                                                # Если False то перебирает все элементы которые остались в
            vmin, kmin = v, k                                   # переменной iterable
            flag = False                                        # Если флаг true (т.е. 1 аргумент в функции) перезаписывает flag и переходит к исполнению строки
        else:                                                   # строки 25
            if k < kmin:                                        # перебирает переменные и перезаписывает минимальные переменные
                vmin, kmin = v, k

    if flag:
        if 'default' in kwargs:
            return kwargs['default']
        raise ValueError('arg is an empty sequence')

    return vmin


empty_sequence = tuple()
value_sequence = 3, 1, 2
x, y, z = value_sequence

print(min(x, y, z))  # result: 1
print(min(value_sequence))  # result: 1

print(min(x, y, z, key=lambda v: -v))  # result: 3
print(min(value_sequence, key=lambda v: -v))  # result: 3

print(min(x, y, z, default=0xE0F))  # result: 1
print(min(value_sequence, default=0xE0F))  # result: 1
print(min(empty_sequence, default=0xE0F))  # result: 3599

print(min(empty_sequence))  # error!