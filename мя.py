import random

n = 20
seq = [random.randint(1,100) for i in range(n)]
print('последовательность', seq)

max_num = []
for number in sorted (seq, reverse = True):
    if len(max_num) == 3:
        break
    if number % 7 == 0:
        max_num.append(number)

if len(max_num) < 3:
    print('в последовательности меньше 3 чисел')
else:
    print(max_num)
