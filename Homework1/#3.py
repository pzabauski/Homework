# Пользователь вводит целое число n. При помощи решета Эрастофена найти все простые числа меньше n

n = 6 #input("Введите целое число")
n = int(n)

seq = []

for i in range(1, 5+1):
    seq.append(i)
print(seq)


j = 0
while j < 5:
    x = seq[j]
    print(x)
    j += 1
    for a in range(1, 5):
        if a % x == 0:
            seq[j] = 0
print(seq)

