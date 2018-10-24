# Модуль string и файлы
# Есть файл с текстом на английском языке.
# 1 Открыть файл, используя функцию open, считать из него текст и вывести на экран.
# 2 Определить количество слов в этом тексте.
# 3 Вывести все буквы, которые используются в этом тексте и сколько раз каждая из них встречается.
# 4 Переставить первую половину строк в тексте со второй и записать обратно в файл.

import string


# 1 Задание 1
# with open('Text.txt') as file:
#    for line in file:
#        print(line.split())
#

# 2 Задание 2
#with open('Text.txt', 'r+') as file:
#    words = 0
#    for line in file:
#        words_in_line = len(line.split())
#        print('words_in_line = %d' % words_in_line)
#        words += words_in_line
#        print('words = %d' % words)
#print(words)

# 3 Задание 3
# Создаем лист уникальных символов из текста

#with open('Text.txt') as file:
#    words = 0
#    characters_in_text = []
#   for line in file:
#        list_of_words = line.split()
#        for word in range(0, len(list_of_words)):
#            words_in_line = list_of_words[word]
#            for character in range(0, len(words_in_line)):
#                if words_in_line[character] not in characters_in_text:
#                    characters_in_text.append(words_in_line[character])
#                else:
#                    continue

#print(characters_in_text)

# Создаем список из слов в тексте (разделитель - пробел)

#list_of_words = []

#with open('Text.txt') as file:
#    for line in file:
#        line_split_1 = line.split()
#        for word in range(0, len(line_split_1)):
#            list_of_words.append(line_split_1[word])
#
#print(list_of_words)

# Создаем словарь содержащий уникальный символы из текста и
# присваиваем каждому из них значение '0'
#d = dict.fromkeys(characters_in_text)
#for i in d:
#    d[i] = 0

# Заполняем словарь частотой с которой слова встречаются в тексте.
#for i in range(0, len(list_of_words)):
#    for j in range(0, len(characters_in_text)):
#        p = list_of_words[i].count(characters_in_text[j])
#        d[characters_in_text[j]] = d[characters_in_text[j]] + p

#print(d)


# 4 Задание 4
