# Модуль random
# Программа загадывает целое число в промежутке [1; 10] (от 1 до 10 включительно) и просит пользователя отгадать его.
# Программа не завершается, пока число не будет отгадано.

import random

x = random.randint(1, 10)

while int(input("Введи число от 1 до 10?")) != x:
    print("Не угадал")
    continue
else:
    print("Угадал")