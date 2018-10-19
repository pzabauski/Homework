# Пользователь вводит целое число n. При помощи решета Эрастофена найти все простые числа меньше n

n = int(input("Введите число"))
seq = []

for i in range(1, n + 1):
    seq.append(i)

print(seq)


for i in range(1, len(seq)):
    x = seq[i]
    if x == 0:
        continue
    for j in range(i+1, len(seq)):
        if seq[j] % x == 0:
            seq[j] = 0

print(seq)


