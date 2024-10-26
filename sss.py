import random

size = int(input('введите размер списка:'))
lst = [] 
for i in range(size):
    if random.random() < 0.8:
        lst.append(1)
    else:
        lst.append(0)

lenght = 0
cur = ''

for num in lst:
    if num == 1:
        cur += 1
        if cur > lenght:
            cur = lenght
    

print(f'список: {lst}')
print(f'самая длинная последовательность: {lenght}')

