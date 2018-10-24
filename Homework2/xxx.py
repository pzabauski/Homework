import string

#help(string)

text = open('Text.txt', 'r+')
t = text.read()
print(t)

string.Formatter.convert_field(t, -1)